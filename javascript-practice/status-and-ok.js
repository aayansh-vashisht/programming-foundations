async function testEndpoints() {
    // 1. Success case (200 OK)
    const goodRes = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    console.log("Status:", goodRes.status); // 200
    console.log("Is OK?:", goodRes.ok);     // true

    // 2. Failure case (404 Not Found)
    // fetch() does NOT crash or jump to a catch block here!
    const badRes = await fetch("https://jsonplaceholder.typicode.com/todos/999999");
    console.log("Status:", badRes.status); // 404
    console.log("Is OK?:", badRes.ok);     // false
}

testEndpoints();