<?php 
  session_start();
  if(!isset($_SESSION['username'])){
    header("Location: ../Workshop2/login.php");
  }
  ?>
<!DOCTYPE html>
<html>
<head>
	<title>Subject</title>
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
  float: right;
  margin-right: 40px;
}
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

*{
    box-sizing: border-box;
  }
input[type=text]{
  width: 90%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  background-color: floralwhite;
}
.ra
{
  text-align: left;
  background-color: floralwhite;
}

</style>
<body>
	<img src="logo.png" width="100px" height="100px" style="float: right;">
	<h1>Automatic OMR Grading</h1>
  <h2>Your grader assistant</h2>
  <br>
  <h2><?=$_SESSION["username"];?></h2>
  <button type="submit" name="submit" onclick="return confirm('Are you sure you want to log out from this page?')"><a href="logout.php">Logout</a></button><br><br>
	<ul>
  <li><a  href="home.php"  name="home">Home</a></li>
  <li><a href="subject.php" style="background-color: honeydew;" name="subject">Subject</a></li>
  <li><a href="student.php" name="student">Student</a></li>
  <li><a href="report.php" name="report">Report</a></li>
</ul>
<br>
<br>
<br>
<p style="text-align: center; font-size: 30px; font-family: monospace;">Add Subject</p>
<div class="container" style=" text-align: center;
    padding: 10px;
    background-color: darkseagreen;
    width: 50%;
    margin: auto;
    font-family: monospace;
    font-size: 20px;
    border-radius: 5px;">

  <form method="post" action="add.php" enctype="multipart/form-data" style="margin: auto;">
    Subject Code:<br> <input type="text" name="subjectcode" required>
      <br><br>
    
      
    Subject Name: <br> <input type="text" name="subjectname" required>
      <br><br>

      <br><br>
      <button onclick="alert('Subject has been added!')"><input type="submit" value="submit" name="submit" ></button> 
</form>
</div>
<br>
<br>
<button><a href="subject.php" style="text-decoration: none";>Back</a></button>

</body>
</html>