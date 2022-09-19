const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movies = data.results;
  for (const i in movies) {
    $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
