// What is the result? Why?

let arr = ["a", "b"];

arr.push(function() {
    console.log( this );
});

arr[2]();


// the code will output the array itself, because `this` refers to array itself.
// When we call a function at arr[2], we just output the array
