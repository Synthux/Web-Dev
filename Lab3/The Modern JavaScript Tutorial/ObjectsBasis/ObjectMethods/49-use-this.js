// Here the function makeUser returns an object.
// What is the result of accessing its ref? Why?

function makeUser() {
    return {
        name: "John",
        ref: this
    };
}

let user = makeUser();

console.log(user.ref);

// The result is the undefined since there is no such attributes
// ref links to global object `window`, it has no `name`