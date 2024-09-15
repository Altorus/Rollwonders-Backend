import {getData, sendData} from "./utils.js";

export async function authentication() {
    const tg = window.Telegram.WebApp;
    const status = await getAuthoriseStatus();
    if (!status) {
        const user = tg.initDataUnsafe.user;
        if (user) {
            let username;
            if (user.username) {
                username = user.username;
            } else {
                username = user.id;
            }
            authoriseUser({"username": username, "telegram_id": user.id});
        }
    }
}

async function getAuthoriseStatus() {
    const res = await getData('/api/authentication/get-status/')
    return res.status;
}

function registerUser(data) {
    sendData(data, "/api/authentication/register/")
        .then(res => {
            console.log(res)
        })
}

function authoriseUser(data) {
    sendData(data, "/api/authentication/login/")
        .then(res => {
            console.log(res)
        })
        .catch(error => {
            registerUser(data)
        })
}