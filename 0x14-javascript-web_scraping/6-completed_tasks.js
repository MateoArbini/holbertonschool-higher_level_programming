#!/usr/bin/node
/*
Write a script that computes the number of tasks completed by user id:
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module axios
*/

const axios = require('axios');
const url = process.argv[2]

axios.get(url)
  .then(response => {
    const dic = {}; // dic to return
    let data = response.data; // var with the data of tasks of each user
    for (let x of data) { // going through each data
        if (x.completed === true) { //if the tasks is completed
            if (dic[x.userId] !== undefined) { //if user is already in dic
                const task_completed = dic[x.userId];
                dic[x.userId] = task_completed + 1;//here we set the value
            } else {
                dic[x.userId] = 1; // if user not in dic, it must be added
                // and we must add the new user with the correspondant value
                // of tasks
            }
          }
        }
        console.log(dic) //print the dic
    })
