const fetchUsers = () => new Promise(res => setTimeout(() => res(["Alice", "Bob"]), 1000));
const fetchPosts = () => new Promise(res => setTimeout(() => res(["Post 1", "Post 2"]), 1000));
const fetchFailingData = () => new Promise((_, rej) => setTimeout(() => rej(new Error("API Down")), 500));

// 1. Sequential (Total time: ~2 seconds)
async function runSequential() {
    const users = await fetchUsers();
    const posts = await fetchPosts();
    console.log("Sequential done:", users, posts);
}

// 2. Parallel with Promise.all (Total time: ~1 second)
async function runParallelAll() {
    try {
        const [users, posts] = await Promise.all([fetchUsers(), fetchPosts()]);
        console.log("Parallel done:", users, posts);
    } catch (err) {
        console.error("One request failed:", err);
    }
}

// 3. Parallel with Promise.allSettled (Safe: returns status for each)
async function runParallelSettled() {
    const results = await Promise.allSettled([fetchUsers(), fetchFailingData()]);

    results.forEach((result, index) => {
        if (result.status === "fulfilled") {
            console.log(`Task ${index} succeeded:`, result.value);
        } else {
            console.log(`Task ${index} failed:`, result.reason.message);
        }
    });
}

runParallelSettled();