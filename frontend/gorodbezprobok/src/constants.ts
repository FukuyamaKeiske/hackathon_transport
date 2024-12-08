import L, { Icon } from "leaflet"
import { ButtonType } from "./types/buttonType"
import { PanelType } from "./types/panelType"

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
            buttonSize: "regular-button",
            destination: "/incidents"
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

export const NOTIFICATIONS: Array<PanelType> = [
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

export const CAMERAS = [
    {
        "name": "Веб-камера у переправы через Обь со стороны Лабытнанги",
        "live_url": "https://video.connect-online.ru/vsaas/embed/pereprava.labytnangi-9eba67ed01?dvr=false&token=3.OSuuHjvCAAAAAAAAAC8ABg1ptjxaGRUY3dQkO2d0ohszYXQ-BH0Y4kTB",
        "geo": "Лабытнанги, Россия",
        "description": "Часовой пояс: GMT+05:00. Качество трансляции: видео 720p.Последняя онлайн проверка: неделю назад (камера онлайн)"
    },
    {
        "name": "Веб-камера на Волгоградском проспекте в Москве",
        "live_url": "https://cameras.inetcom.ru/embed/4",
        "geo": "Москва, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 720p.Последняя онлайн проверка: несколько дней назад (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Железнодорожной улицы и бульвара Алексея Толстого, Пушкин",
        "live_url": "https://rtsp.me/embed/RBQ7BQat/",
        "geo": "Пушкин, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: фото 480p.Последняя онлайн проверка: неделю назад (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Ленина - Дружбы Народов",
        "live_url": "",
        "geo": "Нижневартовск, Россия",
        "description": "Часовой пояс: GMT+05:00. Качество трансляции: видео 360pПоследняя онлайн проверка:  (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Чапаева — Ватутина",
        "live_url": "",
        "geo": "Петрозаводск, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 360p.Последняя онлайн проверка:  (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Шотмана — Ленина",
        "live_url": "",
        "geo": "Петрозаводск, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 360p.Последняя онлайн проверка:  (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Антикайнена — Гоголя",
        "live_url": "",
        "geo": "Петрозаводск, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 360p.Последняя онлайн проверка:  (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Ленина — Андропова",
        "live_url": "",
        "geo": "Петрозаводск, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 360p.Последняя онлайн проверка:  (камера онлайн)"
    },
    {
        "name": "Веб-камера на перекрёстке Лыжная — Балтийская",
        "live_url": "",
        "geo": "Петрозаводск, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 360p.Последняя онлайн проверка:  (камера онлайн)"
    },
    {
        "name": "Перекрёсток Ровио - Парфенова",
        "live_url": "",
        "geo": "Петрозаводск, Россия",
        "description": "Часовой пояс: GMT+03:00. Качество трансляции: видео 360p.Последняя онлайн проверка:  (камера онлайн)"
    }
]

export const FORECASTS = new Map()
    .set("ПРОГНОЗИРУЕМАЯ ПЛОТНОСТЬ ТРАФИКА", "На основе ежеденевных заторов на старокубанском кольце, в период с 7:00-8:00 и 17:00-19:00 ожидается затор")
    .set("ПРОГНОЗИРУЕМАЯ СРЕДНЯЯ СКОРОСТЬ", "24 км/ч")