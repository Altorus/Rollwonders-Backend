export function preloader() {
    window.addEventListener('load', function () {
        var preloader = document.querySelector('#preloader');
        preloader.style.display = 'none';
    });
}