$('.copybtn').click(function() {
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
});
function copythis( lnk ){
    if ( lnk )
    {
        var dummy = document.createElement("textarea");
        document.body.appendChild(dummy);
       
        dummy.value = lnk;
        dummy.select();
        dummy.setSelectionRange(0,99999);
        document.execCommand("copy");
        document.body.removeChild(dummy);
    }
}