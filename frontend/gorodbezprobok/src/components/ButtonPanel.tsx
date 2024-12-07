import { FC } from "react";
import { RegularButtonPanelProps } from "../props/buttonProps";
import { useNavigate } from "react-router-dom";

const ButtonPanel: FC<RegularButtonPanelProps> = ({buttonProperties}) => {
    const navigate = useNavigate()

    const onClickHandler = () => {
        if (buttonProperties.destination === undefined) return
        navigate(buttonProperties.destination)
    }

    return (
        <div className="panel-page-container__button" id={buttonProperties.buttonSize} onClick={() => onClickHandler()}>
            <div className="panel-page-containter_button__elements">
                <img src={buttonProperties.imagePath}/>
                <br/>
                {buttonProperties.title}
            </div>
        </div>
    )
}

export default ButtonPanel