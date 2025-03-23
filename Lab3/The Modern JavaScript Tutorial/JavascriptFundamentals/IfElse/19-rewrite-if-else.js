// Rewrite this if using the conditional operator '?':
// let result;
//
// if (a + b < 4) {
//   result = 'Below';
// } else {
//   result = 'Over';
// }

let a = 3;
let b = 5;

let result = (a + b < 4) ? 'Below' : 'Over';
console.log(result);