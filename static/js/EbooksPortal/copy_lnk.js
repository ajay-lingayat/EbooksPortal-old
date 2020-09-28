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