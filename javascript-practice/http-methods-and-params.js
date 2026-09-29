const BASE_URL = "https://jsonplaceholder.typicode.com";

// 1. GET with Path Parameter (/posts/1)
async function getSinglePost(id) {
    const response = await fetch(`${BASE_URL}/posts/${id}`);
    return response.json();
}

// 2. GET with Query Parameters (/posts?userId=1)
async function getPostsByUser(userId) {
    const params = new URLSearchParams({ userId: userId, _limit: 5 });
    const response = await fetch(`${BASE_URL}/posts?${params}`);
    return response.json();
}

// 3. POST - Create new post
async function createPost(postData) {
    const response = await fetch(`${BASE_URL}/posts`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(postData),
    });
    return response.json();
}

// 4. PATCH - Partially update post
async function updatePostTitle(id, newTitle) {
    const response = await fetch(`${BASE_URL}/posts/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: newTitle }),
    });
    return response.json();
}

// 5. DELETE - Remove post
async function deletePost(id) {
    const response = await fetch(`${BASE_URL}/posts/${id}`, {
        method: "DELETE",
    });
    return response.ok;
}