SQL Injection works as follows-
1. Suppose in the backend, which is likely in PHP or some other language, we use something like
<?php
	$username = $_GET['username']; // kchung
	$result = mysql_query("SELECT * FROM users WHERE username='$username'");
?>
Here username is what we enter into the textbox into our site. Now if we enter ' or '1'='1 (notice the placement of quotes. Copy this exactly.). This will turn into "SELECT * FROM users WHERE username='' or '1'='1'" which effectively gives us all the users. So this is how it works.
Solution to prevent injection - The backend code must check that the input box does not contain ' or some other weird characters.
https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/
https://retrolinuz.wordpress.com/2018/02/18/ctf-ctflearn-com-basic-injection/