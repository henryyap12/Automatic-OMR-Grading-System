<?php 
  session_start();
  if(!isset($_SESSION['username'])){
  	header("Location: ../Workshop2/login.php");
  }

?>
<h2><?php=$_SESSION["username"];?></h2><br><br>
<?php

$id = $_GET['id'];
$dbname = "users";
$conn = mysqli_connect("localhost", "root", "", "automaticomr");

if (!$conn){
	die("Connection failed:" . mysqli_connect_error());
}

$sql = "DELETE FROM users WHERE userid = $id";

if (mysqli_query($conn, $sql)) {
	mysqli_close($conn);
	header('Location: home.php');
	exit;
}
else{
	echo "Error deleting record";
}
?>