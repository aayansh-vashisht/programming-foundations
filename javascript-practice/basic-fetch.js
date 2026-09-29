async function getTodo() {
    // Step 1: Wait for server response headers
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");

    // Step 2: Read and parse the JSON payload
    const data = await response.json();

    console.log("Task title:", data.title);
}

getTodo();