//1
function parameter(name) {
    return `Hello, ${name}!`
}
// Another function that accepts a function as a parameter
function main(func, name) {
    const x = func(name);
    console.log(x);
}
main(parameter, "Namitha");
//2
const a=(firstName,LastName) =>(firstName[0]+LastName[0]);
console.log(a("Roger","Waters"));