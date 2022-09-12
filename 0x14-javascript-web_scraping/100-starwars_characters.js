#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module axios
*/

const axios = require('axios');
const movies = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${movies}`)
  .then(response => {
    for (const x in response.data.characters) {
      axios.get(response.data.characters[x])
        .then(response => {
          console.log(response.data.name);
        });
    }
  });
