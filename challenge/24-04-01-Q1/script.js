async function fetchPosts() {
  try {
    const response = await fetch("./data/input/posts.json");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(`에러 발생: ${error}`, error);
  }
}

for (let i = 1; i <= 10; i++) {
  const option = document.createElement("option");
  option.value = i;
  option.textContent = `작성자 ${i}`;
  document.getElementById("authorFilter").appendChild(option);
}

const listTemplate = ({ userId, id, title, body }) => {
  return `<div> <h3>${id}.${title} 작성자 ${userId}<h3><p>${body}</p></div>`;
};

const postList = document.querySelector("#postList");

function renderPosts(posts) {
  postList.innerHTML = "";
  posts.forEach((item) => {
    postList.insertAdjacentHTML("beforeend", listTemplate(item));
  });
}

async function init() {
  const posts = await fetchPosts();
  renderPosts(posts);

  document
    .getElementById("authorFilter")
    .addEventListener("change", function () {
      const selectedAuthor = this.value;
      if (selectedAuthor === "all") {
        renderPosts(posts);
      } else {
        renderPosts(posts.filter((post) => post.userId === +selectedAuthor));
      }
    });
}

init();
