export function accordion() {
    const accordionItems = document.querySelectorAll('.accordion-item')

    if(accordionItems) {
        accordionItems.forEach(item => {
            item.addEventListener('click', () => {
                const findBodyElem = item.querySelector('.accordion-item__body');
                let otherIsActive = false;
                accordionItems.forEach(el=>{
                    if(el !== item && el.classList.contains('show')) {
                        const elBody = el.querySelector('.accordion-item__body');

                        el.classList.remove('show');
                        elBody.style.maxHeight = null;

                        otherIsActive = true;
                    }
                });
                if(item.classList.contains('show') && !otherIsActive) {
                    item.classList.remove('show');
                    findBodyElem.style.maxHeight = null;
                } else if(!item.classList.contains('show')) {
                    item.classList.add('show');
                    findBodyElem.style.maxHeight = findBodyElem.scrollHeight * 2 + "px";
                }
            });
        });
    }
}

// Для корректной работы необходимо подключить и активировать эту функцию в app.js

// Пример подключения: import { accordion } from "./путь/к/файлу/accordion.js";

// Активация: accordion();