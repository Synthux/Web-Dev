const assert = require('chai').assert;
function pow(x, n) {
    return Math.pow(x, n);
}

// What’s wrong in the test of pow below?
it("Raises x to the power n", function () {
    let x = 5;

    let result = x;
    assert.equal(pow(x, 1), result);

    result *= x;
    assert.equal(pow(x, 2), result);

    result *= x;
    assert.equal(pow(x, 3), result);
});

// more than one test in one it() block
// if the test fail, we will not know which test is incorrect

// npx mocha Lab3/JavasriptInfo/CodeQuality/TestingMocha/43-what-is-wrong-with-test.js
