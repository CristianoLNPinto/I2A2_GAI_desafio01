document.getElementById('sign-in-form').addEventListener('submit', function (event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username === 'cristiano' && password === 'i2a2@GAI') {
        window.location.href = 'product_list.html';
    } else {
        alert('Invalid username or password');
    }
});
