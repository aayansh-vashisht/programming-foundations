const controller = new AbortController();
const signal = controller.signal;

async function searchProducts(searchTerm) {
    try {
        console.log(`Searching for "${searchTerm}"...`);

        // Pass the signal to fetch so it knows when to terminate
        const response = await fetch(`https://dummyjson.com/products/search?q=${searchTerm}`, { signal });
        const data = await response.json();
        console.log("Search results:", data.products);
    } catch (err) {
        if (err.name === "AbortError") {
            console.log("Request was safely aborted by the user/component.");
        } else {
            console.error("Network error:", err.message);
        }
    }
}

// Trigger request
searchProducts("phone");

// Simulate the user navigating away or typing a new letter after 50ms
setTimeout(() => {
    controller.abort(); // Cancels the request immediately
}, 50);