<?php 
  session_start();
  if(!isset($_SESSION['username'])){
    header("Location: ../Workshop2/login.php");
  }
  ?>
<!DOCTYPE html>
<html>
<head>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="../../../assets/css/include.css">
</head>
	<title>Admin home page</title>
</head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: darkseagreen;
  color: black;
}

li {
  float: left;
}

li a, .dropbtn {
  display: inline-block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover, .dropdown:hover .dropbtn {
  background-color: cadetblue;
}

li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #f1f1f1;}

.dropdown:hover .dropdown-content {
  display: block;
}
h1{
  font-family: monospace;
  font-size: 50px;
  margin: 1px;
}
h2{
  margin: 1px;
  font-size:25px;
}
button{
	border:none;
	float: right;

}
/*img{
  width: 3%;
  float: right;
  margin-right: 20px;
}*/
.topnav .search-container {
  float: right;
}

.topnav input[type=text] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}

.topnav .search-container button {
  float: right;
  padding: 6px;
  margin-top: 8px;
  margin-right: 16px;
  background: #ddd;
  font-size: 17px;
  border: none;
  cursor: pointer;
}

.topnav .search-container button:hover {
  background: #ccc;
}

@media screen and (max-width: 600px) {
  .topnav .search-container {
    float: none;
  }
  .topnav a, .topnav input[type=text], .topnav .search-container button {
    float: right;
    display: block;
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 14px;
  }
  .topnav input[type=text] {
    border: 1px solid #ccc;  
  }
  table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  padding: 8px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

</style>
<body>
<div class="jumbotron" style="margin-bottom:0px;margin-top:0px;background-color:#4ABDAC">
	<img src="logo.png" width="100px" height="100px" style="float: right;">
	<h1 style="font-size:60px;color:white">Automatic Omr Grading</h1>
	<h2 style="font-size:20px;color:white">Your Grade Assitant</h2> <br>
	 <h2 style="color:white">Mr <?=$_SESSION["username"];?></h2>  
	 <button class="btn" type="submit" name="submit" onclick="return confirm('Are you sure you want to log out from this page?')"><a href="logout.php" style="color:white">Logout</a></button>
</div>
<ul>
  <li><a href="home.php" style="background-color: honeydew;" name="user">User</a></li>
  <li><a href="reportadmin.php" name="reportadmin">Report</a></li>

</ul>
<br>
<br>
<br>
<div class="container">
<table>
    <tr>
      <th>UserID</th>
      <th>Username</th>
      <th>Email</th>
      <th>Password</th>
      <th>User type</th>
      <th>Delete</th>
      <th>Update</th>
    </tr>
    <?php
    $conn = mysqli_connect("localhost", "root", "", "automaticomr");
    if ($conn-> connect_error) 
    {
      die ("Connection failed: ". $conn-> connect_error);
    }
    ?>
  <?php

    $sql = "SELECT userid, username, email, password, usertype from users";
    $result = $conn-> query($sql);

    if ($result-> num_rows > 0)
    {
      while ($row = mysqli_fetch_assoc($result))
      {
        echo "<tr>";
        echo "<td>".$row['userid']."</td>";
        echo "<td>".$row['username']."</td>";
        echo "<td>".$row['email']."</td>";
        echo "<td>".$row['password']."</td>";
        echo "<td>".$row['usertype']."</td>";
        echo "<td><a href = 'delete.php?id=".$row['userid']."'>Delete</a></td>";
        echo "<td><a href = 'update.php?id=".$row['userid']."'>Update</a></td>";
        echo "</tr>";
      }
      echo "</table>";
    }
    else
    {
      echo "0 result";
    }
    $conn-> close();

    ?>
  </table><br><br>
 </div>


<br>

</body>
</html>