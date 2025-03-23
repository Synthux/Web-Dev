// The input is an array of numbers, e.g. arr = [1, -2, 3, 4, -9, 6].
//
// The task is: find the contiguous subarray of arr with the maximal sum of items.
//
// Write the function getMaxSubSum(arr) that will return that sum.

function getMaxSubSum(arr) {
    let maxSum = 0;
    let currentSum = 0;

    for (let num of arr) {
        currentSum = Math.max(num, currentSum + num);
        maxSum = Math.max(maxSum, currentSum);
    }

    return maxSum;
}