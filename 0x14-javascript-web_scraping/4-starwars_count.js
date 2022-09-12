#!/usr/bin/node
/*
Write a script that prints the number of movies where the character
“Wedge Antilles” is present:
The first argument is the API URL of the
Star wars API: https://swapi-api.hbtn.io/api/films/
Wedge Antilles is character ID 18 - your script must use
this ID for filtering the result of the API
You must use the module axios
*/

const axios = require('axios');
const url = process.argv[2]

axios.get(url)
  .then(response => {
    let totalmovies = 0;
    const movies = response.data.results;
    for (const x in movies) {
      const characters = movies[x].characters;
      for (const j in characters) {
        if (characters[j].includes('18')) {
          totalmovies = totalmovies + 1;
          break;
        }
      }
    }
    console.log(totalmovies);
  })
  .catch(error => {
    console.log(error.response.status);
  });
