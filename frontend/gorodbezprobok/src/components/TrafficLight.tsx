import { FC } from "react";
import { TrafficLightProps } from "../props/trafficLightProps";

const TrafficLightComponent: FC<TrafficLightProps> = ({trafficLightData}) => {
    return (
        <div className="panel__notifications__notification">
            <b>{trafficLightData.id}</b><br/><br/>
            Состояние: {trafficLightData.current_state}<br/>
            Рекомендация: {trafficLightData.recommendedAction}
        </div>
    )
}

export default TrafficLightComponent