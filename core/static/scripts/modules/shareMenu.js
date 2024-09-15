export function shareMenu() {
    const button = document.querySelector('.__openShareMenu');
    if (button) {
        button.addEventListener('click', (e) => {
            const recipeName = document.querySelector('.__recipeName').innerText;

            if (navigator.share) {
                navigator.share({
                    title: recipeName,
                    text: "Сочные рецепты в сервисе Rollwonders",
                    url: window.location.href
                })
                    .then(() => console.log('Successful share'))
                    .catch(error => console.log('Error sharing:', error));
            }
        })
    }
}