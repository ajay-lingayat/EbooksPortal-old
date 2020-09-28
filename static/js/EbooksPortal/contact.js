$(document).ready(function(){

    setvalues();

});

function setvalues(){
    var labels = document.querySelectorAll('form label');
    var inputs = document.querySelectorAll('form input');
    
    for ( i in labels ){
        if (labels[i].getAttribute('for')){
            var text = labels[i].getAttribute('data-text');
            j = parseInt(i)+1;
            if ( j != 5 ){
                inputs[j].setAttribute('value', text);
            }
            else{
                var message = document.getElementById('id_message');
                message.innerHTML = text;
            }
        }
    }
}