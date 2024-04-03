$(document).ready(function(){
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
        var titles = data.results.map(function(film) {
            return film.title;
        });
        $("#list_movies").text(titles.join(", "));
    });
});
