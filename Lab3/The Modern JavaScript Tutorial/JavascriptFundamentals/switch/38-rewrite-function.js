// Rewrite the function using '?' or '||'
// The following function returns true if the parameter age is greater than 18.
//
// Otherwise it asks for a confirmation and returns its result.

function checkAge(age) {
    if (age > 18) {
        return true;
    } else {
        return confirm('Did parents allow you?');
    }
}


// operator ?
function checkAge(age) {
    return (age > 18) ? true : confirm('Did parents allow you?');
}

// operator ||
function checkAge(age) {
    return (age > 18) || confirm('Did parents allow you?');
}