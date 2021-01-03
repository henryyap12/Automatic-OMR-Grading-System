<?php 
	session_start();

	if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("login.php");
    exit;
}

	// variable declaration
	$username = "";
	$email    = "";
	$password_1 ="";
	$password_2 ="";
	//$errors = "";
	$errors = array(); 
	$_SESSION['success'] = "";

	// connect to database
	$db = mysqli_connect('localhost', 'root', '', 'automaticomr');

	// REGISTER USER
	if (isset($_POST['reg_user'])) {
		// receive all input values from the form
		$username = mysqli_real_escape_string($db, $_POST['username']);
		$email = mysqli_real_escape_string($db, $_POST['email']);
		$password_1 = mysqli_real_escape_string($db, $_POST['password_1']);
		$password_2 = mysqli_real_escape_string($db, $_POST['password_2']);
	
		// form validation: ensure that the form is correctly filled
		if (empty($username)) { array_push($errors, "Username is required"); }
		if (empty($email)) { array_push($errors, "Email is required"); }
		if (empty($password_1)) { array_push($errors, "Password is required"); }
		else
		{
					if (isset($password_1) != $password_2) {
			array_push($errors, "The two passwords do not match");
		}
		}
		// if(strlen(trim($password_1)) < 6)
		// {
		// 	array_push($errors, "Password must have at least 6 character");
		// }



	$sql_u = "SELECT * FROM users WHERE username='$username'";
  	$sql_e = "SELECT * FROM users WHERE email='$email'";
  	$res_u = mysqli_query($db, $sql_u);
  	$res_e = mysqli_query($db, $sql_e);

  	if (mysqli_num_rows($res_u) > 0) {
  	  $name_error = "Username already taken, please choose another one"; 	
  	  echo "Sorry, the username is already taken. Please choose another one";
  	}else if(mysqli_num_rows($res_e) > 0){
  	  $email_error = "Sorry... email already taken"; 
  	  echo "Email is already registered.";	
  	}else{

		// register user if there are no errors in the form
		// if (count($errors) == 0) {

  		if(empty($errors) && ($password_1 == $password_2) )
  		{
			$password = md5($password_1);//encrypt the password before saving in the database
			$query = "INSERT INTO users (username, email, password) 
					  VALUES('$username', '$email', '$password')";
			mysqli_query($db, $query);


			$_SESSION['username'] = $username;
			$_SESSION['success'] = "You are now logged in";

			header('location: ../Workshop2educator/home.php');
			// include("../maincust/home.php");
		}
	}
  	}



	// ... 

	// LOGIN USER
	if (isset($_POST['login_user'])) {
		$username = mysqli_real_escape_string($db, $_POST['username']);
		$password = mysqli_real_escape_string($db, $_POST['password']);

		if (empty($username)) {
			array_push($errors, "Username is required");
		}
		if (empty($password)) {
			array_push($errors, "Password is required");
		}

		if (count($errors) == 0) {
			$password = md5($password);
			$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
			$results = mysqli_query($db, $query);

			if (mysqli_num_rows($results) == 1) {
				$_SESSION['username'] = $username;
				$sqltype = "SELECT usertype FROM users WHERE username = '$username'";
				$gettype = mysqli_query($db,$sqltype);
				if(mysqli_num_rows($gettype) === 1)
				{
					$fetchtype = mysqli_fetch_assoc($gettype);
				    $usertype = implode($fetchtype);
				}
				if($usertype === "admin")
				{
					$_SESSION['success'] = "You are now logged in";
				header('location: ../Workshop2admin/home.php');
				}
				// else if ($usertype === "seller")
				// {
				// 	$_SESSION['success'] = "You are now logged in";
				// header('location: ../MainSeller/home.php');
				// }
				else {
				$_SESSION['success'] = "You are now logged in";
				sleep(3);
				header('location: ../Workshop2educator/home.php');}
				// include("../maincust/home.php");
			}else {
				array_push($errors, "Wrong username/password combination");
			}
		}
	}
?>