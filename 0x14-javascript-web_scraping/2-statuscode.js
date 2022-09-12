#!/usr/bin/node
/*
Write a script that display the status code of a GET request:
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
You must use the module axios
Page: https://zetcode.com/javascript/axios/
      https://nodejs.dev/en/learn/error-handling-in-nodejs/
*/

const axios = require('axios');

axios.get(process.argv[2])
  .then(response => {
    console.log(response.status);
  })
  .catch(error => {
    console.log(error.response.status);
  });

