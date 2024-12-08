import { FC, useEffect, useState } from "react";
import { getTimePeriods } from "../utils/utils";
import { useNavigate } from "react-router-dom";


import 'leaflet/dist/leaflet.css';
import "../styles/MapPage.css"
import { Map, TrafficControl, YMaps } from "@pbe/react-yandex-maps";
import Panel from "../components/Panel";
import { useFunctionalActions } from "../hooks/useFunctionalActions";
import { Notification } from "../types/api/notification";

const MapPage: FC = () => {
    const context = useFunctionalActions()
    const [changedNotifications, setChangedNotifications] = useState<Array<Notification>>([]);
    const navigate = useNavigate()

    useEffect(() => {
        const setNotifications = async () => {
            setChangedNotifications(await context.getNotifications())
        }
        setNotifications()
    })

    const onClickHandler = (event: any) => {
        let timePeriod = getTimePeriods(new Date()).get(event.currentTarget.id)
        if(timePeriod === undefined) return
        setChangedNotifications(changedNotifications.filter(notification => notification.timestamp >= timePeriod))
    }

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
                    <div className="panel__date-sorting">
                        <button className="date-sorting__button" id="day" onClick={e => onClickHandler(e)}>Сегодня</button>
                        <button className="date-sorting__button" id="week" onClick={e => onClickHandler(e)}>Неделя</button>
                        <button className="date-sorting__button" id="month" onClick={e => onClickHandler(e)}>Месяц</button>
                    </div>
                    <div className="panel__notifications">
                        { 
                           Array.isArray(changedNotifications) ? (
                                changedNotifications.map(notification =>
                                    <Panel panelData={{title: notification.driver_id, description: notification.message, time: new Date()}}/>
                            )
                           ) : (
                                <a style={{textAlign: "center"}}>Уведомления отсутствуют</a>
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

export default MapPage