const title = "https://swapi-api.alx-tools.com/api/films/?format=json"
$.get(title, function(data) {
    for (const movie of data.results) {
        $("#list_movies").append("<li>" + movie.title + "</li>");
    }
});