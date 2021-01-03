<?php
session_start();
session_destroy();
header('Location:../Workshop2/login.php');
?>