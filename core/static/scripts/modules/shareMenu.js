export function shareMenu() {
    const button = document.querySelector('.__openShareMenu');
    if (button) {
        button.addEventListener('click', (e) => {
            if (navigator.share) {
                navigator.share({
                    title: "Поделиться рецептом",
                    text: "Поделиться рецептом",
                    url: window.location.href
                })
                    .then(() => console.log('Successful share'))
                    .catch(error => console.log('Error sharing:', error));
            }
        })
    }
}