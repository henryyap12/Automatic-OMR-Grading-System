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
	<title>Educator home page</title>
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
  <li><a style="background-color: honeydew;" href="home.php"  name="home">Home</a></li>
  <li><a href="subject.php" name="subject">Subject</a></li>
  <li><a href="student.php" name="student">Student</a></li>
  <li><a href="report.php" name="report">Report</a></li>
  <!-- <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn"></a>
    <div class="dropdown-content">
      <a href="documentary.php">Documentary</a>
      <a href="romance.php">Romance</a>
      <a href="horror.php">Horror</a>
      <a href="family.php">Family</a>
      <a href="action.php">Action</a>
      <a href="fantasy.php">Fantasy</a>
      <a href="science.php">Science Fiction</a>
    </div>
    </li> -->
<!--     <li>
<div class="topnav">
  <div class="search-container">
    <form action="home.php" method="post">
      <input type="text" placeholder="Search.." name="valueToSearch">
      <button type="submit" name="search">Submit</button>
    </form>
  </div>
</div>
</li> -->
</ul>
<br>
<br>
<br>
<h2 style="text-align: center;">What is Automatic OMR Grading System?</h2><br><br>
<div class="row" style="width:100%">
<div class="col-sm-3"></div>
<img src="1.jpeg" alt="1" width="300px" height="200px">
<img src="2.jpeg" alt="2" width="300px" height="200px">
<img src="3.jpeg" alt="3" width="300px" height="200px">
</div>
<br>
<p style="text-align: center; font-size: 20px">There are thousands of answer sheets need to be examined by educators each time schools or universities are having their examination week.</p>
<p style="text-align: center; font-size: 20px">Therefore, this system allows educators to save their time by not grading those sheets manually because it takes too much time to be marking</p> 
<p style="text-align: center; font-size: 20px">one sheet at a time. Also, the system does not cost much and easy to use</p>
</body>
</html>