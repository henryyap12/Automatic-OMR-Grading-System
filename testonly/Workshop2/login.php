<?php include('server.php') ?>
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
</head>

<head>
	<title>Automatic OMR Grading System</title>
</head>
<style>
	body{
		font-family: Arial, Helvetica, sans-serif;
	}
	*{
		box-sizing: border-box;
	}
	.container {
		padding: 10px;
		
		width: 30%;
		margin: auto;
	}
	input[type=text], input[type=password], input[type=email]
	{
  		width: 100%;
  		padding: 10px;
  		margin: 5px 0 22px 0;
  		display: inline-block;
  		border: none;
  		background: #f1f1f1;
	}
	input[type=text]:focus,, input[type=email], input[type=password]:focus 
	{
  		background-color: #ddd;
  		outline: none;
  		text-align: center;
  		margin: auto;
	}
	button{
		background-color: #4CAF50;
		color: white;
		padding: 16px 20px;
		margin: 8px 0;
		border: none;
		cursor: pointer;
		width: 30%;
		opacity: 0.9;
	}
</style>
<body>
<div class="jumbotron" style="margin-bottom:0px;margin-top:0px;background-color:#4ABDAC">
<h1 style="font-size:60px;color:white">Automatic Omr Grading</h1>
<h2 style="font-size:20px;color:white">Your Grade Assitant</h2> 
</div>
  <br>
	<style>
	h1,h2{
		font-family: monospace;
  		font-size: 100px;
  		margin: 1px;
	}
	h2{
		margin: 1px;
  		font-size:25px;
	}
	h3{
		font-family: monospace;
		font-size: 45px;
		margin: 2px;
		text-align: center;
	}
</style>
	<div class="header">
		<h3>LOGIN</h3>
	</div><br>
	
	<form method="post" action="login.php">

		<?php include('errors.php'); ?>

		<div class="container">
			<label>Username</label><br>
			<input type="text" placeholder="Enter username" name="username" >
			<br>
		
			<label>Password</label><br>
			<input type="password" placeholder="Enter password" name="password">
			<p>
			Not yet a member? <a href="register.php" >Sign up</a>
			</p>
			<button type="submit" class="btn  btn-success" name="login_user">Login</button>
		</div>
	</form>


</body>
</html>