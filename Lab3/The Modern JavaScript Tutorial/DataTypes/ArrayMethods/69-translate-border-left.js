// Write the function camelize(str) that changes dash-separated words like “my-short-string” into camel-cased “myShortString”.
//
// That is: removes all dashes, each word after dash becomes uppercased.

function camelize(line) {
    line = line.split('-');
    let result = '';

    for (let w of line) {
        result += w[0].toUpperCase() + w.slice(1);
    }
    return result;
}

console.log(camelize("my-short-string"));       // "myShortString"
console.log(camelize("background-color"));      // "backgroundColor"
console.log(camelize("list-style-image"));      // "listStyleImage"
console.log(camelize("hello-world"));           // "helloWorld"
console.log(camelize("simple"));                // "simple"

