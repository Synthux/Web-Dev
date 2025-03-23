// What are results of these expressions?
console.log("" + 1 + 0);
console.log("" - 1 + 0);
console.log(true + false);
console.log(6 / "3");
console.log("2" * "3");
console.log(4 + 5 + "px");
console.log("$" + 4 + 5);
console.log("4" - 2);
console.log("4px" - 2);
console.log("  -9  " + 5);
console.log("  -9  " - 5);
console.log(null + 1);
console.log(undefined + 1);
console.log(" \t \n" - 2);

// "" + 1 + 0       = "10"
// "" - 1 + 0       = -1
// true + false     = 1
// 6 / "3"          = 2
// "2" * "3"        = 6
// 4 + 5 + "px"     = "9px"
// "$" + 4 + 5      = "$45"
// "4" - 2          = 2
// "4px" - 2        = NaN
// "  -9  " + 5     = "  -9  5"
// "  -9  " - 5     = -14
// null + 1         = 1
// undefined + 1    = NaN
// " \t \n" - 2     = -2
