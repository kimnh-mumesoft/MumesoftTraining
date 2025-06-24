const menu = document.querySelector(".menu");
const sidebar = document.querySelector(".sidebar");
const closeBtn = document.querySelector(".close");
const overlay = document.querySelector(".overlay");
const themeBtn = document.querySelector("#theme-btn");
const langContainer = document.querySelector(".lang-container");
const langBtns = document.querySelectorAll(".lang-btn");
const langList = document.querySelector(".lang-list");
const htmlElement = document.documentElement;

menu.addEventListener("click", (e) => {
  sidebar.classList.toggle("active");
});

closeBtn.addEventListener("click", (e) => {
  sidebar.classList.remove("active");
});

overlay.addEventListener("click", (e) => {
  sidebar.classList.remove("active");
});

themeBtn.addEventListener("click", () => {
  if (htmlElement.getAttribute("data-theme") === "dark") {
    htmlElement.setAttribute("data-theme", "light");
  } else {
    htmlElement.setAttribute("data-theme", "dark");
  }
});

langBtns.forEach((btn) =>
  btn.addEventListener("click", (e) => {
    e.stopPropagation();
    langList.classList.toggle("show");
  })
);

langList.addEventListener("click", (e) => {
  e.stopPropagation();
  console.log(e.target.getAttribute("data-lang"));

  langBtns.forEach((btn) => {
    if (btn.getAttribute("data-lang") === e.target.getAttribute("data-lang")) {
      btn.classList.add("show");
    } else {
      btn.classList.remove("show");
    }
  });

  langList.classList.remove("show");
});

window.addEventListener("click", (e) => {
  if (langList.classList.contains("show")) {
    if (!langContainer.contains(e.target)) {
      langList.classList.remove("show");
    }
  }
});
