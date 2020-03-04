const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);

$(function(){

    $('#search').keyup(function(){

        $.ajax({
            type: "POST",
            url: "/articles/search/",
            data: {
                'search_text': $('#search').val(),
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val()
            },
            success: searchSuccess,
            dataType: 'html'
        });

    });

});

function searchSuccess(data, textStatus, jqXHR){
    $('#search-results').html(data)
}