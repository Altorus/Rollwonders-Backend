export function popup() {
    const popupButtons = document.querySelectorAll('.__openPopup');
    if (popupButtons.length > 0) {
        popupButtons.forEach(button => {
            button.addEventListener('click', event => {
                const type = button.dataset.popuptype;
                openPopup(type);
            })
        })
    }

    const ctaMobile = document.querySelectorAll('.cta-button-mobile');
    if (ctaMobile.length > 0) {
        ctaMobile.forEach(btn => {
            let startedMove = 0;
            const menu = btn.closest('.popup');
            let startedTop = 0;
            btn.addEventListener('touchstart', (event) => {
                const startOfMove = event.touches[0].clientY;

                startedMove = startOfMove;
                startedTop = menu.style.top;
            });
            btn.addEventListener('touchmove', (event) => {
                const move = event.touches[0].clientY;
                if (startedMove < move) {
                    menu.style.top = 'auto';
                    menu.style.bottom = (window.innerHeight - move - menu.offsetHeight) + 'px';
                }
                ;
            });
            btn.addEventListener('touchend', (event) => {
                const endOfMove = event.changedTouches[0].clientY;
                if (startedMove < endOfMove + 100) {
                    closeAllMenus();
                    menu.style.top = null;
                    menu.style.bottom = null;
                } else {
                    menu.style.top = startedTop;
                    menu.style.bottom = null;
                }
            });
        });
    }
}

const inset = document.querySelector('.__inset');
const body = document.querySelector('body');

inset.addEventListener('click', () => {
    closeAllMenus();
})

function closeAllMenus() {
    const popups = document.querySelectorAll('.popup');
    popups.forEach(popup => {
        popup.classList.remove('show');
        inset.classList.remove('show');
    })
    body.style.overflow = "auto";
}

function openPopup(type) {
    const popup = document.querySelector(`[data-popuptype="${type}"]`);
    if (!popup) return

    popup.classList.add('show');
    inset.classList.add('show');
    body.style.overflow = "hidden";
}
