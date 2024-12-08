import { FC } from "react";
import { format } from "date-fns"
import { PanelProps } from "../props/panelProps";

const Panel: FC<PanelProps> = ({panelData}) => {
    return (
        <div className="panel__notifications__notification">
            <b>{panelData.title}</b><br/><br/>
            {panelData.description}<br/>
            {format(panelData.time, "dd.MM.yyyy")}
        </div>
    )
}

export default Panel