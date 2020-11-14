let a = document.querySelector('.a');
let body = document.querySelector('body');
a.onclick = function() {
    body.classList.toggle('dark');
}
