export function themeManager() {
    const body = document.querySelector('body');
    const tg = window.Telegram.WebApp;
    const colorScheme = tg.colorScheme


    if (localStorage.getItem("switchedTheme") === 'true') {
        body.classList.add('dark-theme');
    } else if (!localStorage.getItem("switchedTheme")) {
        if (colorScheme === 'light') {
            body.classList.remove('dark-theme');
        } else {
            body.classList.add('dark-theme');
        }
    } else {
        body.classList.remove('dark-theme');
    }

    const button = document.querySelector('.__changeTheme')
    if (button) {
        button.addEventListener('click', (e) => {
            if (!body.classList.contains('dark-theme')) {
                localStorage.setItem("switchedTheme", "true");
            } else {
                localStorage.removeItem("switchedTheme");
            }
            body.classList.toggle('dark-theme');
        })
    }
}