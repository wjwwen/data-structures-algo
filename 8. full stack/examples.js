// EXAMPLE 1
let uni = "NTU";
let course = "MSBA";
console.log(uni + course); 
console.log(uni.indexOf("N")); //1
console.log(uni.indexOf("Z")); //-1
console.log(uni.includes("N")); //true
console.log(uni.includes("Z")); //false
console.log(`I am studing in ${uni} taking ${course}`); //formatted text in python

// EXAMPLE 2
console.log(null == undefined); //true
console.log(null === undefined); //false
console.log(!null); //true
console.log(!undefined); //true
console.log(!!null); //false
console.log(!!undefined); //false

// 0.1 + 0.2 != 0.3!
// 0.1 + 0.2 = 0.0000004. Extra decimal due to inaccuracy in representing numbers

// EXAMPLE 3
let a = {};
a.uni = "NTU";
a.years = 2;

console.log("University: " + a.uni);
console.log("Years: " + a.years);
console.log(a.course); //outputs

// EX