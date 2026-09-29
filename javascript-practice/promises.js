function checkInventory(item) {
    return new Promise((resolve, reject) => {
        const inStock = true; // toggle to false to test rejection

        setTimeout(() => {
            if (inStock) {
                resolve(`${item} is in stock!`);
            } else {
                reject(new Error(`${item} is out of stock.`));
            }
        }, 1000);
    });
}

checkInventory("Laptop")
    .then((message) => {
        console.log("Success:", message);
    })
    .catch((error) => {
        console.error("Error:", error.message);
    })
    .finally(() => {
        console.log("Inventory check complete.");
    });