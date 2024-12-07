import { FC } from "react";
import "../styles/PanelPage.css"
import { PANEL_BUTTONS, SMALL_BUTTONS } from "../constants";
import ButtonPairs from "../components/ButtonPairs";
import ButtonPanel from "../components/ButtonPanel";

const PanelPage: FC = () => {
    return (
        <>
        <div className="title-containers">
            <div className="panel-page-container" id="title-container">
                CityFlow
            </div>
            <div className="panel-page-container" id="menu-container">
                <img src="/public/images/TOCHKI).png"/>
                Главное меню
            </div>
        </div>
        
        <div className="panel-page-container" id="functional-panel">
            {
                PANEL_BUTTONS.map(pairButtons =>
                    <ButtonPairs pairs={pairButtons}/>
                )
            }

            <div id="pair-buttons">
                <ButtonPanel
                    buttonProperties={{
                        title: "Светофоры",
                        imagePath: "/public/images/traffic_light.png",
                        buttonSize: "regular-button"
                    }}
                />
                <div className="pagel-page-container__small-buttons">
                    {
                        SMALL_BUTTONS.map(smallButton =>
                            <ButtonPanel buttonProperties={smallButton}/>
                        )
                    }
                </div>
            </div>
        </div>
        </>
    )
}

export default PanelPage