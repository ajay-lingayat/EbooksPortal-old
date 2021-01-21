function mark_download( URL ){
    $.ajax({
        url: URL,
        data: {},
        dataType: 'JSON',
        success: function(data){
            if ( data.ans ){
                console.log('done!');
            }
        }
    });
}