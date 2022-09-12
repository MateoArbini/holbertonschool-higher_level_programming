#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file:
The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module axios
*/

const axios = require('axios');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

axios.get(url)
  .then(response => {
    const text = response.data;
    fs.writeFile(file, text, err => {
      if (err) {
        console.log(err);
      }
    });
  });
