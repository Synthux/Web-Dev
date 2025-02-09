// Create a function truncate(str, maxlength) that checks the length of the str and, if it exceeds maxlength – replaces the end of str with the ellipsis character "…", to make its length equal to maxlength.
// The result of the function should be the truncated (if needed) string.

function truncate(line, maxlength) {
    if (line.length > maxlength) {
        return line.slice(0, maxlength -1) + "…";
    }
    return line;
}

console.log(truncate("Hello, world!", 10));                 // "Hello, w…"
console.log(truncate("Hi", 5));                             // "Hi"
console.log(truncate("JavaScript is awesome", 17));         // "JavaScript is a…"