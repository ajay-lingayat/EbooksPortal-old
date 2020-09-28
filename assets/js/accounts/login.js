$(document).ready(function(){
    setupinputs();
});


function setupinputs(){
    var username = document.getElementById('id_login');
    username.setAttribute('class', 'form-control');

    var password = document.getElementById('id_password');
    password.setAttribute('class', 'form-control');

    var chkbox = document.getElementById('id_remember');
    chkbox.setAttribute('checked','');
    chkbox.style.display = 'none';
}