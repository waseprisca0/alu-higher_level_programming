#!/usr/bin/node

const argu = process.argv.slice(2);
if (argu.length <= 1) {
  console.log(0);
} else {
  console.log(argu.sort((a, b) => b - a)[1]);
}
