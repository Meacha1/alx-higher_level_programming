$(document).ready(function() {
    $('#btn_translate').click(function() {
        translateHello();
    });

    $('#language_code').keypress(function(event) {
        if (event.keyCode == 13) {
            translateHello();
        }
    });
});

function translateHello() {
    var languageCode = $('#language_code').val();
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode;

    $.getJSON(apiUrl, function(data) {
        $('#hello').html(data.hello);
    });
}