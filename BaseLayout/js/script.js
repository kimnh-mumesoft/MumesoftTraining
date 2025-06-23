const menu = document.querySelector(".menu");
const sidebar = document.querySelector(".sidebar");
const closeBtn = document.querySelector(".close");
const overlay = document.querySelector(".overlay");

menu.addEventListener("click", (e) => {
  sidebar.classList.toggle("active");
});

closeBtn.addEventListener("click", (e) => {
  sidebar.classList.remove("active");
});

overlay.addEventListener("click", (e) => {
  sidebar.classList.remove("active");
});

window.addEventListener("resize", () => {
  const viewportWidth = window.innerWidth;

  if (viewportWidth >= 1200) {
    if (sidebar.classList.contains("active")) {
      sidebar.classList.remove("active");
    }
  }
});
