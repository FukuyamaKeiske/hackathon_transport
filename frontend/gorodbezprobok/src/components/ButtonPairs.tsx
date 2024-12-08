import { FC } from "react";
import { ButtonPairsProps } from "../props/buttonPairsProps";

import ButtonPanel from "./ButtonPanel";

const ButtonPairs: FC<ButtonPairsProps> = ({pairs}) => {
    return (
        <div id="pair-buttons">
            {
                pairs.map(button => 
                    <ButtonPanel buttonProperties={button}/>
                )
            }
        </div>
    )
}

export default ButtonPairs