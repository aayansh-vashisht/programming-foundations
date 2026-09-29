// Synchronous: runs in order immediately
console.log("1: Ordering coffee");

// Asynchronous: offloaded to the browser timer API
setTimeout(() => {
    console.log("2: Coffee ready (picked up after wait)");
}, 1000);

// Synchronous: runs while the browser handles the timer
console.log("3: Checking phone while waiting");

// Output Order:
// 1: Ordering coffee
// 3: Checking phone while waiting
// 2: Coffee ready (picked up after wait)