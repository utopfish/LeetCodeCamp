Promise.resolve().then(function promise1 () {
    console.log('promise1');
 })
setTimeout(function setTimeout1 (){
 console.log('setTimeout1')
 Promise.resolve().then(function  promise2 () {
    console.log('promise2');
 })
}, 0)

setTimeout(function setTimeout2 (){
console.log('setTimeout2')
}, 0)


// 循环1：

// 【task队列：script ；microtask队列：】


// 从task队列中取出script任务，推入栈中执行。
// promise1列为microtask，setTimeout1列为task，setTimeout2列为task。


// 【task队列：setTimeout1 setTimeout2；microtask队列：promise1】


// script任务执行完毕，执行microtask checkpoint，取出microtask队列的promise1执行。

// 循环2：
// *【task队列：setTimeout1 setTimeout2；microtask队列：】
// 4. 从task队列中取出setTimeout1，推入栈中执行，将promise2列为microtask。

// 【task队列：setTimeout2；microtask队列：promise2】


// 执行microtask checkpoint，取出microtask队列的promise2执行。

// 循环3：

// 【task队列：setTimeout2；microtask队列：】


// 从task队列中取出setTimeout2，推入栈中执行。
// 7.setTimeout2任务执行完毕，执行microtask checkpoint。


// 【task队列：；microtask队列：】

