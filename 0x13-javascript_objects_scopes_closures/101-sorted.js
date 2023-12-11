#!/usr/bin/node
// A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
const dict = require('./101-data').dict;
const newDiction = {};

Object.keys(dict).map(function (key, index) {
  if (newDiction[dict[key]] === undefined) {
    newDiction[dict[key]] = [];
  }
  newDiction[dict[key]].push(key);
});

console.log(newDiction);
