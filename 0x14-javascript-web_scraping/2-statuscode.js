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

async function makeRequest () {
  const config = {
    method: 'GET',
    url: process.argv[2]
  };
  try {
    const res = await axios(config);
    console.log(res.status);
  } catch (err) {
    console.error(err.response.status);
  }
}

makeRequest();
