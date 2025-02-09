function extractCurrencyValue(str) {
    return Number(str.replace("$", ""));
}

console.log(extractCurrencyValue("$120"));          // 120
console.log(extractCurrencyValue("$99.99"));        // 99.99
console.log(extractCurrencyValue("$0"));            // 0