export function modals() {
    const allModals = document.querySelectorAll(".modal");

    document.querySelectorAll('.open-modal').forEach(button => {
        button.addEventListener('click', (e) => {
            const modalValue = e.target.dataset.typeModal;
            const modalElement = document.querySelector(`[data-type="${modalValue}"]`);
            modalElement.dataset.modalState = "open";
            document.documentElement.style.overflow = "hidden";
        });
    });

    document.querySelectorAll('.btn-modal-close, .modal-inset').forEach(closeButton => {
        closeButton.addEventListener('click', closeModal);
    });

    function closeModal() {
        allModals.forEach((el) => {
            el.dataset.modalState = "close";
        });
        document.documentElement.style.overflow = null;
    }
}


// Для корректной работы необходимо подключить и активировать эту функцию в app.js

// Пример подключения: import { modals } from "./путь/к/файлу/modals.js";

// Активация: modals();