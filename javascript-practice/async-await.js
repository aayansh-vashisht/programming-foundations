function fetchPrice(productId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (productId === 404) {
                reject(new Error("Product not found"));
            } else {
                resolve(49.99);
            }
        }, 1000);
    });
}

async function displayCheckout(productId) {
    try {
        console.log("Fetching price...");
        // Execution inside this function pauses here until fetchPrice resolves
        const price = await fetchPrice(productId);
        console.log(`Item price: $${price}`);
    } catch (error) {
        // Catches errors thrown by any rejected promise inside the try block
        console.error("Checkout failed:", error.message);
    } finally {
        console.log("Checkout workflow finished.");
    }
}

displayCheckout(101); // Success path
// displayCheckout(404); // Failure path