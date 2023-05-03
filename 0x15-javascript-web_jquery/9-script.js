const hello = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(hello, function(data) {
    $("#hello").text(data.hello);
});