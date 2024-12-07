import { FC } from "react";
import "../styles/AuthorizationPage.css"


const AuthorizationPage: FC = () => {
    return (
        <>
        <div className="title-containers">
            <div className="login-page-container" style={{height: "104px", width: "194px", marginRight: "31px"}} id="title-container">
                CityFlow
            </div>
            <div className="login-page-container" style={{height: "104px", width: "389px"}} id="title-container">
                РЕГИСТРАЦИЯ ИЛИ ВХОД
            </div>
        </div>
        <div className="login-page-container" style={{height: "790px", width: "614px"}} id="login-forms-container">
            <a>Введите свои электронную почту и пароль</a>
            <input className="login-page-container__form" placeholder="Email:" id="login-page-container__form__email"/>
            <input className="login-page-container__form" placeholder="Пароль:" type="password" id="login-page-container__form__password"/>
            <div className="login-page-container__button">
                <img src="/public/images/login_image.png"/>
                ВОЙТИ
            </div>
            <div className="login-page-container__button" id="sign-up-button">
                <img src="/public/images/login_image2.png"/>
                ЗАРЕГИСТРИРОВАТЬСЯ
            </div>
            <a className="sad">Нужна наша помощь или забыли пароль?</a>
        </div>
        </>
    )
}

export default AuthorizationPage