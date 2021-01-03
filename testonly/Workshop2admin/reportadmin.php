<?php 
  session_start();
  if(!isset($_SESSION['username'])){
    header("Location: ../Workshop2/login.php");
  }
  ?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <title>Report for admin</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="../../../assets/css/include.css">
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title><?php include("include/tabTitle.php"); ?></title>
    <link rel="shortcut icon" href="images/iconTab.ico" type="image/x-icon">
    <!-- Bootstrap Styles-->
    <link href="assets/css/bootstrap.css" rel="stylesheet" />
    <!-- FontAwesome Styles-->
    <link href="assets/css/font-awesome.css" rel="stylesheet" />
    <!-- Custom Styles-->
    <link href="assets/css/custom-styles.css" rel="stylesheet" />
    <!-- Google Fonts-->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css' />
	
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
  <body>
<div class="jumbotron" style="margin-bottom:0px;margin-top:0px;background-color:#4ABDAC">
  <img src="logo.png" width="100px" height="100px" style="float: right;">
  <h1 style="font-size:60px;color:white">Automatic Omr Grading</h1>
  <h2 style="font-size:20px;color:white">Your Grade Assitant</h2> <br>
   <h2 style="color:white">Mr <?=$_SESSION["username"];?></h2>  
   <button class="btn" type="submit" name="submit" onclick="return confirm('Are you sure you want to log out from this page?')"><a href="logout.php" style="color:white">Logout</a></button>
</div>
<ul>
  <li><a href="home.php" name="user">User</a></li>
  <li><a href="reportadmin.php"  style="background-color: honeydew" name="reportadmin">Report</a></li>

</ul>

<script>
<!-- function print-->

function myFunction() {
    window.print();
}
</script>

<?php
	$con = mysqli_connect('localhost','root','','automaticomr') or Die();
?>
<html>
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
   <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script> 
    



    
  

            
 <!-- TOTAL SERVICE BY DATE-->    
     <script type="text/javascript">
    google.load("visualization", "1", {packages:["corechart"]});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([

          ['User', 'Total User'],
            <?php 
	        	$query = "	SELECT  usertype, count(usertype) FROM users  group by usertype asc";

	        	$exec = mysqli_query($con,$query);
	        	while($row = mysqli_fetch_array($exec)){

	        		echo "['".$row['usertype']."',".$row['count(usertype)']."],";
	        	}
	   ?>
         
        ]);

        var options = {
        	title: 'TOTAL USERS'
        };
      var chart = new google.visualization.ColumnChart(document.getElementById("columnchart2"));
      chart.draw(data, options);
  }
  </script>  

     <!-- TOTAL DEBT or PAID-->     
  
  </head>
  <body>
  <div class="container">
  <button><a href="home.php" class="w3-bar w3-light-grey w3-round w3-display-bottom middle w3-show-small w3-button">Back</a></button>
<button class="w3-bar w3-light-grey w3-round w3-display-bottom middle w3-show-small w3-button" onClick="myFunction()">Print</button></br></br><table width="200" border="1">
     <tr align="center">
      <center> 
       <td><h3>BAR CHART ON TOTAL USERS</h3>
   <div id="columnchart2" style="width: 700px; height: 500px;"></div></td>
    </tr>
     
    
     

   </table>
   
   
   
  
   
   
</div>
</body>
</html>
				
				
				
				
				
				
					
            
            <!-- /. PAGE INNER  -->
        </div>
        <!-- /. PAGE WRAPPER  -->
    </div>
    <!-- /. WRAPPER  -->
    <!-- JS Scripts-->
    <!-- jQuery Js -->
    <script src="assets/js/jquery-1.10.2.js"></script>
    <!-- Bootstrap Js -->
    <script src="assets/js/bootstrap.min.js"></script>
    <!-- Metis Menu Js -->
    <script src="assets/js/jquery.metisMenu.js"></script>
    <!-- Custom Js -->
    <script src="assets/js/custom-scripts.js"></script>

	<script>
	Morris.Bar({
		
		element : 'chart',
		data: [<?php echo $chart_data; ?>],
		xkey:'year',
		ykey : ['profit', 'purchase', 'sale'],
		labels  : ['profit', 'purchase', 'sale'],
		hideHover : 'auto', 
	});
	</script>
	
	
	
</body>
</html>
