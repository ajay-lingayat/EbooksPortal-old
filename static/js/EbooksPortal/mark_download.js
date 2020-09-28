
function mark_download( bk_id ){
    $.ajax({
        url: '/books/mark-download',
        data: {
            'bk_id': bk_id
        },
        dataType: 'JSON',
        success: function(data){
            if ( data.ans ){
                console.log('done!');
            }
        }
    });
}