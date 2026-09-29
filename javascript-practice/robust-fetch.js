async function fetchUserProfile(userId) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);

        // If the server returned 404, 500, etc., bail out immediately
        if (!response.ok) {
            throw new Error(`Request failed: ${response.status}`);
        }

        // Only parse JSON if the response was actually successful
        const user = await response.json();
        console.log("User Name:", user.name);
        return user;
    } catch (error) {
        // Catches BOTH network failures AND HTTP status errors we threw manually
        console.error("Fetch failed:", error.message);
    }
}

// Successful request
fetchUserProfile(1);

// Failing request (userId 9999 does not exist -> triggers our custom throw)
fetchUserProfile(9999);