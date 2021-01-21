function mark_download( URL, redirectURL ){
    $.ajax({
        url: URL,
        data: {},
        dataType: 'JSON',
        success: function(data){
            if ( data.ans ){
                window.location.href = redirectURL;
            }
            else {
                snack('Something went wrong! Please try again.');
            }
        },
        error: function(error) {
            snack('Something went wrong! Please try again.');
        }
    });
}

function snack(message) {
    document.getElementById('toast-message').innerHTML = message;
    $('#copied').addClass("fade");
    $('#copied').addClass("show");
    $('#copied').removeClass("hide");
    setTimeout(function() {
        var e = document.getElementById('copied');
        e.classList.remove('show');
        e.classList.add('hide');
    },
    5000);
    $(".close").click(function() {
        $('#copied').addClass("hide");
        $('#copied').removeClass("show");
    });
}