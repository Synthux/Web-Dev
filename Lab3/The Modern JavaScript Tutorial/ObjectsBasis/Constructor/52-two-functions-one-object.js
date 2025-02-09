// Is it possible to create functions A and B so that new A() == new B()?
//
// function A() { ... }
// function B() { ... }
//
// let a = new A();
// let b = new B();
//
// alert( a == b ); // true
//
// If it is, then provide an example of their code.


// Yes, it's possible. You can make both A and B return the same object;
let obj = {};

function A() {
    return obj;
}

function B() {
    return obj;
}

console.log(new A() == new B()); // true