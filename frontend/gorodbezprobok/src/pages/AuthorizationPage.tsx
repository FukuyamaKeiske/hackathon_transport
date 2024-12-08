import { ChangeEvent, FC, useState } from "react";
import { useAuthActions } from "../hooks/useAuthActions";
import { useNavigate } from "react-router-dom";

import "../styles/AuthorizationPage.css"

const AuthorizationPage: FC = () => {
    const authActionsContext = useAuthActions()
    const navigate = useNavigate()
    const [email, setEmail] = useState<string>('')
    const [password, setPassword] = useState<string>('')
    const [errorMessage, setErrorMessage] = useState<string>('')

    const onChangeHandler = (event: ChangeEvent<HTMLInputElement>) => {
        if (event.currentTarget.type === "email") setEmail(event.currentTarget.value)
        else if (event.currentTarget.type === "email") setPassword(event.currentTarget.value)
    }

    const onSignInSubmitHandler = async () => {
        setErrorMessage("Во время авторизации произошла ошибка")
        const response = await authActionsContext.signIn(email, password)
        if(response === true) {
            navigate("/")
        } else {
            setErrorMessage("Во время авторизации произошла ошибка")
        }
    }

    return (
        <>
            <div className="title-containers">
                <div className="login-page-container" style={{height: "104px", width: "194px", marginRight: "31px"}} id="title-container">
                    CityFlow
                </div>
                <div className="login-page-container" style={{height: "104px", width: "389px"}} id="title-container">
                    ВХОД В АККАУНТ
                </div>
            </div>
            <div className="login-page-container" style={{height: "790px", width: "614px"}} id="login-forms-container">
                <a>Введите свои электронную почту и пароль</a>
                <input className="login-page-container__form" type="email" placeholder="Email:" id="login-page-container__form__email" onChange={onChangeHandler}/>
                <input className="login-page-container__form" placeholder="Пароль:" type="password" id="login-page-container__form__password" onChange={onChangeHandler}/>
                <div className="login-page-container__button" id="sign-in-button" onClick={onSignInSubmitHandler}>
                    <img src="/public/images/login_image.png"/>
                    ВОЙТИ
                </div>
                {errorMessage && <div style={{ color: 'red' }}>{errorMessage}</div>}
                <a className="sad">Нужна наша помощь или забыли пароль?</a>
            </div>
        </>
    )
}

export default AuthorizationPage