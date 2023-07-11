document.getElementById('forgot-password-form').addEventListener('submit', function (event) {
    event.preventDefault();

    var email = document.getElementById('email').value;

    if (email) {
        if (validateEmail(email)) {
            var successMessage = 'O link para redefinição da senha foi enviado para o endereço ' + email;
            alert(successMessage);
            window.location.href = 'index.html';
        } else {
            alert('Invalid email');
        }
    } else {
        alert('Please enter your email');
    }
});

function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}