const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');

togglePassword.addEventListener('click', function () {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    this.classList.toggle('bx-show');
    this.classList.toggle('bx-hide');
});
// Retrieve the username and password input fields
    var usernameInput = document.getElementById("username");
    var passwordInput = document.getElementById("password");

    // Check if there is a saved password and populate the fields
    if (localStorage.getItem("savedUsername") && localStorage.getItem("savedPassword")) {
        usernameInput.value = localStorage.getItem("savedUsername");
        passwordInput.value = localStorage.getItem("savedPassword");
    }

    // Add an event listener to the form submission
    document.querySelector("form").addEventListener("submit", function(event) {
        // Check if the "Remember Me" checkbox is selected
        if (document.getElementById("remember").checked) {
            // Save the username and password in localStorage
            localStorage.setItem("savedUsername", usernameInput.value);
            localStorage.setItem("savedPassword", passwordInput.value);
        } else {
            // Clear the saved username and password from localStorage
            localStorage.removeItem("savedUsername");
            localStorage.removeItem("savedPassword");
        }
    });