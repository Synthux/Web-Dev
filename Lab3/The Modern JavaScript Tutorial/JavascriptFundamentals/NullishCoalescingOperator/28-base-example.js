let height = 0;

console.log(height || 100);     // 100
console.log(height ?? 100);     // 0
console.log(null ?? height);    // 0
