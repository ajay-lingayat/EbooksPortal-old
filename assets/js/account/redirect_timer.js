$(document).ready(function(){
	var element = document.getElementById('login_url');
	login_url = element.getAttribute('login_url');
	setTimeout("location.href = '"+login_url+"'",10000);
});