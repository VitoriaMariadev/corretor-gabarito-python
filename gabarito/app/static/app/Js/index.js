// togglePassword.js
function togglePassword() {
    var passwordField = document.getElementById('password');
    var passwordFieldIcon = document.getElementById('eyeIcon');
    console.log(passwordFieldIcon)

    if (passwordField.type === "password") {
        passwordField.type = "text";
        passwordFieldIcon.src = "{% static 'app/Images/eyeClose.svg' %}";
    } else {
        passwordField.type = "password";
        passwordFieldIcon.src = "{% static 'app/Images/eye.svg' %}";
    }
}
