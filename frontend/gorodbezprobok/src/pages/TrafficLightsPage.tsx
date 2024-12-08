import { FC } from "react";
import { useNavigate } from "react-router-dom";


import 'leaflet/dist/leaflet.css';
import "../styles/MapPage.css"
import { Map, TrafficControl, YMaps } from "@pbe/react-yandex-maps";
import TrafficLightComponent from "../components/TrafficLight";
import { TrafficLight } from "../types/api/trafficLight";

const TrafficLightsPage: FC = () => {
    const navigate = useNavigate()
    const trafficLights: Array<TrafficLight> = [
        {
            id: "sddsf",
            current_state: "sdfdsf",
            recommendedAction: "sdfsdf"
        },
        {
            id: "sddsf",
            current_state: "sdfdsf",
            recommendedAction: "sdfsdf"
        },
        {
            id: "sddsf",
            current_state: "sdfdsf",
            recommendedAction: "sdfsdf"
        },
    ]

    return (
        <>
            <div className="map-panel-container">
                <div className="map-panel-container__map">
                <YMaps>
                    <Map defaultState={{ center: [45.03913263910287,38.976724473573235], zoom: 9 }} style={{ width: "1229px", height: "945px"}}>
                        <TrafficControl options={{ float: "right" }}/>
                    </Map>
                </YMaps>
                </div>
                <div className="map-panel-container__panel">
                    <div className="map-title">
                        <img src="/public/images/map.png"/>
                        Карта
                    </div>
                    <div className="panel__notifications">
                        {
                            trafficLights.map(trafficLight =>
                                <TrafficLightComponent trafficLightData={trafficLight}/>
                            )
                        }
                    </div>
                    <div className="panel__back" onClick={() => navigate("/")}>
                        НАЗАД
                    </div>
                </div>
            </div>
        </>
    )

}

export default TrafficLightsPage