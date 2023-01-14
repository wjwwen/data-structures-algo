// Msg and Puzzle as elements
let b = {};
let puzzle = "msg";
b[puzzle] = "where does this go?";
b.puzzle = "is this in the same place?";
console.log(b);

// ----- Javascript - If ------
const date = new Date(); 

let day = date.getDate();
let month = date.getMonth() + 1; // Since January starts from 0, need to +1
let year = date.getFullYear();

// This arrangement can be altered based on how we want the date's format to appear.
let currentDate = `${day}-${month}-${year}`;
// This arrangement can be altered based on how we want the date's format to appear.
console.log(currentDate); // "17-6-2022"

if (month == 12){
    console.log("Merry Christmas")
}
else if (month ==2 ){ // nested if else statement
    console.log("Happy Lunar New Year")}
else {
    console.log(`Happy ${year}`)
}

// ----- Javascript - Looping ------
let number = 0;
while(number<=12){
    console.log(number);
    number = number + 2;
}

let result = 1;
for (let counter = 0; counter < 10; counter = counter + 1){
    result = result * 2 
}

// ----- Javascript - Break ------
for (let current = 20; ; current = current + 1) { if (current % 7 == 0) {
    console.log(current);
break; }
else{
console.log(`testing ${current} not divided by 7`)
}
}

// ----- Javascript - Block ------
// Global vs local variable. Printing different As

let a = 199;
for (let current = 20, a =0; ; current++) { if (current % 7 == 0) {
        console.log(current);
break; }
else{
console.log(`testing ${current} not divided by 7`) 
a++;
console.log(`found ${a}`)
} }
console.log(`a is ${a}`)

// ----- Side Effects ------
// Whatever that is updated in the function will be updated in the "let" in the first line
let latestGreeting = "";
function greet( name ) { 
    console.log( `Hello ${name}` ); 
    latestGreeting = name;
}
greet( "Skywalker" );
greet( "Vader" ); 
console.log( latestGreeting );

// ----- Structured values: array ------
// Not changing Days, but changing the content of one of the element
const DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]; 
console.log(DAYS);
console.log(DAYS[0]);
DAYS[1]=2;
console.log(DAYS); 
console.log(DAYS[1]); 
console.log(DAYS.length)

