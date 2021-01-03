<?php 
  session_start();
  if(!isset($_SESSION['username'])){
    header("Location: ../Workshop2/login.php");
  }
  ?>
  <?php
    $conn = mysqli_connect("localhost", "root", "", "automaticomr");
    if ($conn-> connect_error) 
    {
      die ("Connection failed: ". $conn-> connect_error);
    }
    // $subjectcode = $_POST['subjectcode'];
   $username = $_SESSION["username"];
    $sqlid = "SELECT userid FROM users WHERE username = '$username'";
    $getid = $conn-> query($sqlid);
    if ($getid-> num_rows === 1)
    {
      $fetchid = mysqli_fetch_assoc($getid);
      $userid = implode($fetchid);
    }
    $subjectcode = $_GET["subjectcode"];
    $sub = "SELECT subjectcode FROM subject WHERE subjectcode = '$subjectcode'";
    $getsub = $conn-> query($sub);
    if ($getsub-> num_rows ===1)
    {
      $fetchsub = mysqli_fetch_assoc($getsub);
      $subjectcode = implode($fetchsub);
    }

    $sql = "SELECT * from student WHERE userid = '$userid' AND subjectcode = '$subjectcode'";
    $result = $conn-> query($sql);
  ?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="../../../assets/css/include.css">
	<title>Display student of that userid</title>
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
	<h2 style="font-size:20px;color:white">Your Grade Assitant</h2> 
	 <h2 style="color:white">Mr<?=$_SESSION["username"];?></h2>  
	 <button class="btn" type="submit" name="submit" onclick="return confirm('Are you sure you want to log out from this page?')"><a href="logout.php" style="color:white">Logout</a></button>
</div><ul>
  <li><a  href="home.php"  name="home">Home</a></li>
  <li><a href="subject.php"  name="subject">Subject</a></li>
  <li><a href="student.php" style="background-color: honeydew;" name="student">Student</a></li>
  <li><a href="report.php" name="report">Report</a></li>
</ul>
<br>
<br>
<br>

  <h2 style="text-align: center; font-size: 30px; font-family: times new roman;">Student Enrollment</h2><br>
  <table style="border-collapse: collapse;
  width: 100%; border: 1px solid #ddd;
  text-align: left;">
    <tr>
      <th style = "border: 1px solid #ddd;
  text-align: left; padding: 15px;">StudentID</th>
      <th style = "border: 1px solid #ddd;
  text-align: left; padding: 15px;">Student Matric Number</th>
      <th style = "border: 1px solid #ddd;
  text-align: left; padding: 15px;">Student Name</th>
  <th style = "border: 1px solid #ddd;
  text-align: left; padding: 15px;">Mark</th>
      <th style = "border: 1px solid #ddd;
  text-align: left; padding: 15px;">Update Mark</th>
    </tr>
    <?php
$i=0;
while($row = mysqli_fetch_array($result)) {
if($i%2==0)
$classname="even";
else
$classname="odd";
?>
<tr class="<?php if(isset($classname)) echo $classname;?>">
<td><?php echo $row["studentid"]; ?></td>
<td><?php echo $row["studentnumber"]; ?></td>
<td><?php echo $row["studentname"]; ?></td>
<td><?php echo $row["mark"]; ?></td>
<td><a href="#">Scan</a></td>
</tr>
<?php
$i++;
}
?>
<br>
<br>

</table>

<br>
<br>
<br>
<button style="float: right;"><a href="addstudent.php">Add students</a></button>
</body>
</html>