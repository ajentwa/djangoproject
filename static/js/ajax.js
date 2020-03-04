$(function(){

    $('#search').keyup(function(){

        $.ajax({
            type:"POST",
            url:"/articles/search2/",
            data: {
                'search_text': $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: "html"
        })
    })
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-resukts').html(data);
}