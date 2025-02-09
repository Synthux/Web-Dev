// Write a function pow(x,n) that returns x in power n.
// Or, in other words, multiplies x by itself n times and returns the result.

function pow(x, n) {
    let result = x;

    for (let i = 1; i < n; i++) {
        result *= x;
    }

    return result;
}