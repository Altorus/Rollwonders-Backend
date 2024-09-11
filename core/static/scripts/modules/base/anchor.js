export function anchor() {
    const anchorEl = document.querySelectorAll('.anchor__elem');
    anchorEl.forEach((el) => {
        const scrollAttr = el.getAttribute('data-scroll')
        const hiddenElement = document.getElementById(scrollAttr);
        el.addEventListener('click',() => {
            if (hiddenElement) {
                const marginTop = parseInt(window.getComputedStyle(hiddenElement).marginTop);
                const targetPosition = hiddenElement.getBoundingClientRect().top + window.scrollY - marginTop;
            
                window.scrollTo({ top: targetPosition, behavior: "smooth" });
            }
        })
    })
}

// Для корректной работы необходимо подключить и активировать эту функцию в app.js

// Пример подключения: import { anchor } from "./путь/к/файлу/anchor.js";

// Активация: anchor();