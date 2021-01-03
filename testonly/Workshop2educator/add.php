<?php 
  session_start();

  // if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
  //   header("../loginregistrationsystem/login.php");
  //   exit;
  if(!isset($_SESSION['username'])){
    header("Location: ../Workshop2/login.php");
  }

?>
<h2><?=$_SESSION["username"];?></h2>
<?php

    $subjectcode = $_POST['subjectcode'];
    $subjectname = $_POST['subjectname'];

    $conn = mysqli_connect('localhost', 'root', '', 'automaticomr');
    if (!$conn) {
      die ("Connection Failed :" . mysqli_connect_error());
    }

    echo "Connected successfully";
     $username = $_SESSION['username'];
    $query = "SELECT userid FROM users WHERE username='$username'";
        $results=mysqli_query($conn,$query);
        while ($row = mysqli_fetch_array($results))
        {
            $userid = $row['userid'];
        }



      $sql = "INSERT INTO subject (subjectcode, subjectname, userid) 
          VALUES('$subjectcode', '$subjectname', '$userid')";

          if (mysqli_query($conn, $sql)) {
            echo "New record created successfully";
          }
          else{
            echo "Error:" . $sql . "<br>" . mysqli_error($conn);
          }
          mysqli_close($conn);
          header("location: subject.php");
?>

