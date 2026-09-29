// Example: Sending an authentication token in request headers
async function fetchPrivateAccount(authToken) {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/todos/1", {
            headers: {
                // Bearer token identifies the session securely
                "Authorization": `Bearer ${authToken}`,
                "Content-Type": "application/json"
            }
        });

        if (response.status === 429) {
            throw new Error("Rate limit exceeded. Please slow down requests.");
        }

        if (response.status === 401) {
            throw new Error("Token expired or invalid. Please re-authenticate.");
        }

        if (!response.ok) {
            throw new Error(`Fetch failed with status ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        // If CORS fails, the browser blocks access and fetch throws a TypeError
        console.error("Request blocked or failed:", error.message);
    }
}

// Dummy execution
fetchPrivateAccount("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...");