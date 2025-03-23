function checkSpam(str) {
    let lowerStr = str.toLowerCase();
    return lowerStr.includes("viagra") || lowerStr.includes("xxx");
}

console.log(checkSpam("buy ViAgRa now"));       // true
console.log(checkSpam("free xXx videos"));      // true
console.log(checkSpam("hello world"));          // false
