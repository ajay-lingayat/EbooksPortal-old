
function book_mark_download( bk_id ){
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


function paper_mark_download( paper_id ){
    $.ajax({
        url: '/papers/mark-download',
        data: { 
            'paper_id': paper_id
        },
        dataType: 'JSON',
        success: function(data){
            if ( data.ans ){
                console.log('done!');
            }
        }
    });
}