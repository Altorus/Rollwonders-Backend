export function makingRecipeFunctions() {
    const span = document.querySelector('.__makingPercent');
    if (span) {
        let percentage = 0;
        let requestCounter = 0; // Счётчик для запросов

        const interval = setInterval(async () => {
            if (percentage >= 100) {
                clearInterval(interval);
                return;
            }

            // Обновляем процентное значение
            percentage++;
            updatePercentage(percentage);

            // Проверяем, нужно ли делать запрос
            if (percentage % 30 === 0) {
                requestCounter++;
                try {
                    // Предположим, ваш URL выглядит так: http://example.com/?recipe_id=123
                    const url = new URL(window.location.href); // Получаем текущий URL
                    const params = new URLSearchParams(url.search); // Получаем строку запроса

                    const recipeId = params.get('recipe_id');

                    const response = await fetch(`/api/generate-recipe/${recipeId}/`); // Замените на свой URL
                    const result = await response.json();

                    if (result.recipeCreated) {
                        percentage = 100;
                        updatePercentage(percentage);
                        clearInterval(interval);
                    } else if (percentage >= 90) {
                        // Если значение уже 90, замедляем увеличение
                        clearInterval(interval);
                        const slowInterval = setInterval(() => {
                            percentage++;
                            updatePercentage(percentage);
                            if (percentage >= 100) {
                                clearInterval(slowInterval);
                            }
                        }, 600); // Замедленный интервал
                    }
                } catch (error) {
                    console.error('Ошибка запроса:', error);
                }
            }
        }, 100); // Интервал обновления процента

        // Дополнительная проверка каждые 2%
        setInterval(() => {
            if (percentage % 2 === 0 && percentage < 100) {

            }
        }, 1000); // Интервал проверки
    }
}

function updatePercentage(value) {
    const span = document.querySelector('.__makingPercent');
    if (value >= 0 && value <= 100) {
        span.textContent = `${value}%`;
    } else {
        console.error('Значение должно быть в диапазоне от 0 до 100');
    }

    if (value == 100) {
        const url = new URL(window.location.href); // Получаем текущий URL
        const params = new URLSearchParams(url.search); // Получаем строку запроса

        const recipeId = params.get('recipe_id');
        window.location.href = `/recipe/${recipeId}`;
    }
}