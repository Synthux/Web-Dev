// A random integer from min to max
// Create a function randomInteger(min, max) that generates a random integer number from min to max including both min and max as possible values.
// Any number from the interval min..max must appear with the same probability.

function randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}