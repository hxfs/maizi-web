/**
 * Created by jhxfs on 2017/5/10.
 */

$('#search').keyup(function () {
    if($(this).val().length > 0){
        var url = "http://127.0.0.1:8000/search";
        $.ajax({
            url:url,
            type: 'GET',
            data: {'data': $(this).val()},
            dataType: 'json',
            success: function (data){
                console.log('111');
                console.log(data);
            },
            error:function () {
                console.log('333');
            }
        })
    }
});