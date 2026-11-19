let counter = 0

document.querySelectorAll('.horizontal_button').forEach(button => {
    button.addEventListener('click', function() {
        counter ++;
        this.innerHTML = "Hello World!" + counter;
    });
});