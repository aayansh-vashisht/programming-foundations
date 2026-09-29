function fetchUserData(userId, callback) {
    setTimeout(() => {
        console.log("Data retrieved from server");
        callback({ id: userId, username: "alex99" });
    }, 1000);
}

// Passing an inline callback function
fetchUserData(101, (user) => {
    console.log(`Welcome back, ${user.username}!`);
});