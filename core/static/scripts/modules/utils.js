export function debounce(func, timeout) {
    let timer;
    return function() {
        const context = this;
        const args = arguments;
        clearTimeout(timer);
        timer = setTimeout(function() {
            func.apply(context, args);
        }, timeout);
    };
};
export function findParentWithClass(element, className) {
    let parent = element.parentElement;

    while (parent) {
        if (parent.classList.contains(className)) {
            return parent;
        }
        parent = parent.parentElement;
    }

    return null; // Если родительский элемент с указанным классом не найден
}
export async function sendData(data, url) {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': "application/json",
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data),
    });
    if(response.ok) return response.json();
    else throw new Error(response.statusText);
};
export async function getData(url) {
    const response = await fetch(url, {
        method: "GET",
    });
    if(response.ok) return response.json();
    else throw new Error(response.statusText);
};
export const userLoggedIn = () => {
    return document.cookie.replace(/(?:(?:^|.*;\s*)token\s*\=\s*([^;]*).*$)|^.*$/, "$1");
}
export function setNewQuery(key, value) {
    const url = new URLSearchParams(window.location.search);
    url.delete(key);
    if(Array.isArray(value)) {
        url.append(key, value);
    } else {
        if(!!value) url.append(key, value);
    }

    window.location.search = url.toString();
};
export function getCurrentQuery() {
    const queryParams = new URLSearchParams(window.location.search);
    const keysValue = {};
    for (let pair of queryParams.entries()) {
        let key = pair[0];
        let value = pair[1];
        keysValue[`${key}`] = value;
    };
    return keysValue;
}