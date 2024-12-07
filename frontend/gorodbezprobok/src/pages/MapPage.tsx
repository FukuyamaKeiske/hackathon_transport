import { MapContainer, TileLayer } from "react-leaflet";
import { FC, useState } from "react";
import { NOTIFICATIONS } from "../constants";
import { NotificationType } from "../types/notificationType";

import Notification from "../components/Notification";

import 'leaflet/dist/leaflet.css';
import "../styles/MapPage.css"
import { getTimePeriods } from "../utils/utils";
import { useNavigate } from "react-router-dom";

const MapPage: FC = () => {
    const [changedNotifications, setChangedNotifications] = useState<Array<NotificationType>>(NOTIFICATIONS);
    const navigate = useNavigate()

    const onClickHandler = (event: any) => {
        let timePeriod = getTimePeriods(new Date()).get(event.currentTarget.id)
        if(timePeriod === undefined) return
        setChangedNotifications(NOTIFICATIONS.filter(notification => notification.time >= timePeriod))
    }

    return (
        <>
            <div className="map-panel-container">
                <div className="map-panel-container__map">
                    <MapContainer center={[51.505, -0.09]} zoom={13} style={{ width: "1229px", height: "945px"}}>
                        <TileLayer
                            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />
                    </MapContainer>
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
                            changedNotifications.map(notification =>
                                <Notification notificationData={notification}/>
                            )
                        }
                    </div>
                    <div className="panel__back" onClick={() => navigate(-1)}>
                        НАЗАД
                    </div>
                </div>
            </div>
        </>
    )

}

export default MapPage