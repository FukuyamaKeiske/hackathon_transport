import L, { Icon } from "leaflet"
import { ButtonType } from "./types/buttonType"
import { NotificationType } from "./types/notificationType"

import markerShadow from "leaflet/dist/images/marker-shadow.png"

export const RED_MARKER_ICON: Icon = new L.Icon({
    iconUrl: `https://via.placeholder.com/30/FF0000/ffffff?text=+`,
    shadowUrl: markerShadow,
    iconSize: [30, 30],
    iconAnchor: [15, 30],
    popupAnchor: [0, -30],
})

export const GREEN_MARKER_ICON: Icon = new L.Icon({
    iconUrl: `https://via.placeholder.com/30/00FF00/ffffff?text=+`,
    shadowUrl: markerShadow,
    iconSize: [30, 30],
    iconAnchor: [15, 30],
    popupAnchor: [0, -30],
})

export const PANEL_BUTTONS: Array<Array<ButtonType>> = [
    [
        {
            title: "Карта",
            imagePath: "/public/images/map.png",
            buttonSize: "regular-button",
            destination: "/map"
        },
        {
            title: "Инциденты",
            imagePath: "/public/images/incidents.png",
            buttonSize: "regular-button"
        }
    ],
    [
        {
            title: "Прогноз",
            imagePath: "/public/images/time.png",
            buttonSize: "regular-button"
        },
        {
            title: "Мероприятия",
            imagePath: "/public/images/calendar.png",
            buttonSize: "regular-button"
        }
    ],
    [
        {
            title: "Камеры",
            imagePath: "/public/images/camera.png",
            buttonSize: "regular-button",
            destination: "/cameras/1"
        },
        {
            title: "Анализ трафика",
            imagePath: "/public/images/statistics.png",
            buttonSize: "regular-button"
        }
    ]
]

export const SMALL_BUTTONS: Array<ButtonType> = [
    {
        title: "Эффективность",
        imagePath: "/public/images/agile.png",
        buttonSize: "small-button"
    },
    {
        title: "Экология",
        imagePath: "/public/images/leaf.png",
        buttonSize: "small-button"
    }
]

export const NOTIFICATIONS: Array<NotificationType> = [
    {
        title: "уведомление",
        description: "описание уведомления для заполнения текста описание уведомления для заполнения текста",
        time: new Date()
    },
    {
        title: "уведомление",
        description: "описание уведомления для заполнения текста описание уведомления для заполнения текста",
        time: new Date()
    },
    {
        title: "уведомление",
        description: "описание уведомления для заполнения текста описание уведомления для заполнения текста",
        time: new Date()
    },
    {
        title: "уведомление",
        description: "описание уведомления для заполнения текста описание уведомления для заполнения текста",
        time: new Date()
    }
]