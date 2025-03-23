// Write a function ucFirst(str) that returns the string str with the uppercased first character, for instance:

function ucFirst(word) {
    return word[0].toUpperCase() + word.slice(1);
}
console.log(ucFirst("hello Wolrd"))
