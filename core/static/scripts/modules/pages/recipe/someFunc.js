import {sendData} from "../../utils.js";

export function recipeProcessor() {
    const ingredients = document.querySelectorAll(".ingridient-card");
    const button = document.querySelector('.__createRecipe')
    if (ingredients.length && button) {
        ingredients.forEach(ingredient => {
            const checkboxes = ingredient.querySelectorAll("input[type=checkbox]");
            checkboxes.forEach(checkbox => {
                checkbox.addEventListener("change", (element) => {
                    const card = element.target.closest('.ingridient-card');
                    changeIngredientState(card);
                    changeCreateButtonState();
                });
            });
        });

        button.addEventListener('click', event => {
            sendData({"ingredients": getSelectedIngredients()}, '/api/generate-recipe/')
                .then(res => {
                    window.location.href = "/making-recipe/?recipe_id=" + res.recipe_id;
                })
        })
    }

}

function getSelectedIngredients() {
    const checkboxes = document.querySelectorAll(".ingridient-card input[type=checkbox]:checked");
    if (!checkboxes.length) return [];

    return Array.from(checkboxes).map(checkbox => checkbox.value);
}

function changeIngredientState(card) {
    const stateElement = card.querySelector(`.__ingridientState`);
    const checkboxes = card.querySelectorAll('input[type=checkbox]:checked').length;
    if (checkboxes > 0) {
        stateElement.innerText = "Выбрано";
    } else {
        stateElement.innerText = "Не выбрано";
    }
}

function changeCreateButtonState() {
    const cards = document.querySelectorAll(".ingridient-card");
    const hasCard = Array.from(cards).some(card => {
        return card.querySelector('input[type=checkbox]:checked')
    })
    const button = document.querySelector('.__createRecipe')

    button.disabled = !hasCard
}