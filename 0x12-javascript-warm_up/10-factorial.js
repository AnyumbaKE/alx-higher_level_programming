#!/usr/bin/node
// Computes and prints a factorial recursively
function factorial (n) {
    return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
  }
  
  console.log(factorial(Number(process.argv[2])));