const signUpButton = document.getElementById("signup");
const signInButton = document.getElementById("signin");
const continer = document.getElementById("container");

signUpButton.addEventListener("click", () => {
  continer.classList.add("right-panel-activate");
});

signInButton.addEventListener("click", () => {
  continer.classList.add("right-panel-activate");
});
