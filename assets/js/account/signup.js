$(document).ready(function(){
    setupinputs();
});


function setupinputs(){
    var fields = document.querySelectorAll('input');
    for ( i in fields ){
        if (fields[i].getAttribute('id'))
        {
            fields[i].setAttribute('class', 'form-control');
        }
    }
}