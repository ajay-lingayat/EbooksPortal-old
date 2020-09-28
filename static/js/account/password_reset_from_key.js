$(document).ready(function(){
    setupinputs();
});


function setupinputs(){
    var password1 = document.getElementById('id_password1');
    password1.setAttribute('class', 'form-control');

    var password2 = document.getElementById('id_password2');
    password2.setAttribute('class', 'form-control');
}