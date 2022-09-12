#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode
number matches a given integer:
The first argument is the movie ID
You must use the Star wars API with the endpoint:
https://swapi-api.hbtn.io/api/films/:id
You must use the module axios
`` - To reference a var in js, you must use the backsticks in the sentence
     ${var name}
*/

const axios = require('axios');
const episode = process.argv[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${episode}`)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.log(error.response.status);
  });
