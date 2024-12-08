import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import { FC, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";

import { Camera } from "../types/api/camera";
import CameraComponent from "../components/CameraComponent";

import 'leaflet/dist/leaflet.css';
import "../styles/CamerasPage.css"

const CamerasPage: FC = () => {
    const navigate = useNavigate()
    const pages = [1, 2, 3, 4, 5, 6, 7]
    const params = useParams()

    const cameras: Array<Camera> = [
        {
            name: "камера",
            live_url: "https://soundcloud.com/vomitator",
            geo: "45.04095306379043,38.97097790071476",
            description: "камера"
        },
        {
            name: "камера",
            live_url: "https://soundcloud.com/vomitator",
            geo: "43.04095306379043,39.97097790071476",
            description: "камера2"
        },
        {
            name: "камера",
            live_url: "https://soundcloud.com/vomitator",
            geo: "44.04095306379043,40.97097790071476",
            description: "камера2"
        },
        {
            name: "камера",
            live_url: "https://soundcloud.com/vomitator",
            geo: "43.04095306379043,38.97097790071476",
            description: "камера3"
        }
    ]
    
    useEffect(() => {
        if (Number.isNaN(Number(params.page))) navigate("/cameras/1")
        
        const startPage = document.getElementById(params.page!)
        startPage!.style.backgroundColor = "#808080"
        startPage!.style.color = "#FFFFFF"
        startPage!.style.boxShadow = "0px 0px 25px 7px rgba(128, 128, 128, 0.25)"
    })

    const onClickHandler = (event: any) => {
        const startPage = document.getElementById(params.page!)
        startPage!.style.backgroundColor = "rgba(31, 31, 31, 0.00)"
        startPage!.style.color = "#808080"
        startPage!.style.boxShadow = "0px 0px 250px 0px rgba(0, 0, 0, 0.25)"
        navigate(`/cameras/${event.currentTarget.id}`)
    }

    return (
        <>
            <div className="cameras-panel-container">
                <div className="cameras-panel-container__map">
                    <MapContainer center={[45.03913263910287,38.976724473573235]} zoom={13} style={{ width: "1229px", height: "945px"}}>
                        <TileLayer
                            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />
                        {
                            cameras.map((camera) =>
                                <Marker position={[Number(camera.geo.split(",")[0]), Number(camera.geo.split(",")[1])]}>
                                    <Popup>
                                        {camera.description}
                                    </Popup>
                                </Marker>
                            )
                        }
                    </MapContainer>
                </div>
                <div className="cameras-panel-container__panel">
                    <div className="cameras-title">
                        <img src="/public/images/camera.png"/>
                        Камеры
                    </div>
                    <div className="panel__page-sorting">
                        {
                            pages.map((value) => 
                                <button className="page-sorting__button" id={value.toString()} onClick={onClickHandler}>{value}</button>
                            )
                        }
                    </div>
                    <div className="panel__cameras">
                        {
                            cameras.map((value) =>
                                <CameraComponent camerasData={value}/>
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

export default CamerasPage