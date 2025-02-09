// Create a function multiplyNumeric(obj) that multiplies all numeric property values of obj by 2.


function multiplyNumeric(obj) {
    for (let key in obj) {
        if (typeof obj[key] == 'number') {
            obj[key] *= 2;
        }
    }
}