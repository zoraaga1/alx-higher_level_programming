#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId]++;
      } else {
        completedTasksByUser[task.userId] = 1;
      }
    }
  });

  for (const userId in completedTasksByUser) {
    console.log(`User ${userId} has completed ${completedTasksByUser[userId]} tasks`);
  }
});
