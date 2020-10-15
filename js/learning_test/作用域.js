// console.log(foo);
// function foo(){
//     console.log("foo");
// }
// var foo = 1;


// var value = 'tom';
// function foo() {
//     console.log(value)
// }
// function bar() {
//     var value = 'bob';
//     foo();
// }
// bar();


// function foo() {
//     return function() {
//         console.log(this)
//     }
// }
// foo()(); 


var foo = {
    bar: function () {
        return this;
    }
}
foo.bar(); 
