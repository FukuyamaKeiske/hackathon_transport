import { Map, YMaps, TrafficControl } from "@pbe/react-yandex-maps";
import { FC } from "react";
import { useNavigate } from "react-router-dom";

import "../styles/MapPage.css"
import { Incident } from "../types/api/incident";
import Panel from "../components/Panel";

const IncidentsPage: FC = () => {
    const navigate = useNavigate()
    const incidents: Array<Incident> = [
        {
            id: "1sdad",
            description: "ploxo",
            severity: 1,
            timestamp: "08.12.24",
            location: "rossia"
        },
        {
            id: "1sdad",
            description: "ploxo",
            severity: 1,
            timestamp: "08.12.24",
            location: "rossia"
        },
        {
            id: "1sdad",
            description: "ploxo",
            severity: 1,
            timestamp: "08.12.24",
            location: "rossia"
        },
        {
            id: "1sdad",
            description: "ploxo",
            severity: 1,
            timestamp: "08.12.24",
            location: "rossia"
        }
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
                        <img src="/public/images/incidents.png"/>
                        Инциденты
                    </div>
                    <div className="panel__notifications">
                        {incidents.map(incident =>
                            <Panel panelData={{title: incident.id, description: incident.description, time: new Date(incident.timestamp)}}/>
                        )}
                    </div>
                    <div className="panel__back" onClick={() => navigate("/")}>
                        НАЗАД
                    </div>
                </div>
            </div>
        </>
    )

}

export default IncidentsPage