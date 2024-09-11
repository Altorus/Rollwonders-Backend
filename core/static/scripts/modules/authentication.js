import {getData, sendData} from "./utils.js";

export async function authentication() {
    const tg = window.Telegram.WebApp;


    const colorScheme = tg.colorScheme
    const status = await getAuthoriseStatus();
    if (!status) {
        authoriseUser({"username": "79879536376", "telegram_id": 12345});
        // const user = tg.initDataUnsafe.user;
        // if (user) {
        //     console.log(user)
        // }
    }
}

async function getAuthoriseStatus() {
    const res = await getData('/api/authentication/get-status/')
    return res.status;
}

function registerUser(data){
    sendData(data, "/api/authentication/register/")
        .then(res=>{
            console.log(res)
        })
}

function authoriseUser(data){
    sendData(data, "/api/authentication/login/")
        .then(res=>{
            console.log(res)
        })
        .catch(error=>{
            registerUser(data)
        })
}