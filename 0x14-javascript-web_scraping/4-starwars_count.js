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
const url = process.argv[2];

axios.get(url)
  .then(response => {
    let totalmovies = 0; // var which is going to be returned
    const movies = response.data.results;
    // var which contains the total amount of movies - 7
    for (const x in movies) {
      // here we go through all movies
      const characters = movies[x].characters;
      // here we save into a var, the chars of the movies we went through
      for (const j in characters) {
        // we go through all chars we saved previosuly
        if (characters[j].includes('18')) {
          // here we ask if in chars, theres the id 18, which is the one
          // we are looking for
          totalmovies = totalmovies + 1;
          // if it matches, we add 1 to the var that we are returning
          break;
        }
      }
    }
    console.log(totalmovies);
  })
  .catch(error => {
    console.log(error.response.status);
  });
