//setTimeout是异步执行的，会排在任务队列中，只有主线上的全部执行完，
//才会执行任务队列里的任务，当主线执行完成后，i=5，所以打印5次5
// for(var i=0; i<5 ;i++) {
//     setTimeout(() => {
//         console.log(i);
//     })
// }

// setTimeout(() => {console.log(1)}, 0);

// new Promise(resolve => {
//     console.log(2);
//     resolve();
//     Promise.resolve.then(() => {
//         console.log(3);
//     }).then(() => {
//         console.log(4);
//     }).then(() => {
//         console.log(5);
//     })
// })
 
//  console.log(6);


let Parent = function (name, age) {
    this.name = name;
    this.age = age;
};
Parent.prototype.sayName = function () {
    console.log(this.name);
};
//自己定义的new方法
let newMethod = function (Parent, ...rest) {
    // 1.以构造器的prototype属性为原型，创建新对象；
    let child = Object.create(Parent.prototype);
    // 2.将this和调用参数传给构造器执行   
    let result = Parent.apply(child, rest);
    // 3.如果构造器没有手动返回对象，则返回第一步的对象
    return typeof result  === 'object' ? result : child;
};

const child = newMethod(Parent, 'echo', 26);
child.sayName() //'echo';

