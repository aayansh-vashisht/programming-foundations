async function registerUser(username, email) {
    const payload = { username, email };

    const response = await fetch("https://jsonplaceholder.typicode.com/users", {
        method: "POST",
        // Request Headers tell the server how to interpret the raw body string
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        // Request Body: converted from JS Object to JSON string
        body: JSON.stringify(payload)
    });

    // Checking status codes
    console.log("HTTP Status Code:", response.status); // 201 Created

    if (!response.ok) {
        throw new Error(`Server returned error: ${response.status}`);
    }

    // Response Body: read and parsed from JSON stream
    const responseData = await response.json();
    console.log("Server created record:", responseData);
}

registerUser("johndoe", "john@example.com");