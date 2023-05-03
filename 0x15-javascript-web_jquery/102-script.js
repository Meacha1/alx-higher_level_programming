$(document).ready(function() {
    const url = "https://www.fourtonfish.com/hellosalut/hello/";
    $('INPUT#btn_translate').click(function() {
        var lang = $('#language_code').val();
        $.get(url + lang, function(response) {
            $('#hello').text(response.hello);
        });
        console.log(response);
    });
});