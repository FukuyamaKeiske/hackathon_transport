import { Axios } from "axios";
import { User } from "../types/api/user";
import { Incident } from "../types/api/incident";
import { Forecast } from "../types/api/forecast";
import { Camera } from "../types/api/camera";
import { Waypoint } from "../types/api/waypoint";
import { TrafficAnalysis } from "../types/api/trafficAnalysis";
import { TrafficLight } from "../types/api/trafficLight";
import { Notification } from "../types/api/notification";

export class Http {
    axios = new Axios({
        baseURL: import.meta.env.VITE_API_URL
    })

    async signUp(email: string, password: string): Promise<number> {
        const response = await this.axios.post<User>(
            "/api/v1/sign-up",
            {
                "email": email,
                "password": password
            }
        )
        return response.status
    }

    async signIn(email: string, password: string): Promise<User | undefined> {
        const response = await this.axios.post(
            "/api/v1/sign-in",
            {
                "email": email,
                "password": password
            }
        )
        if (response.status !== 200) return
        localStorage.setItem("token", response.data.token)
        return response.data.token
    }

    async getIncidents(): Promise<Array<Incident>> {
        return (await this.axios.get<Array<Incident>>("/api/v1/incidents")).data
    }

    async getIncident(incidentId: string): Promise<Incident | undefined> {
        const response = await this.axios.get<Incident>(`/api/v1/incidents/${incidentId}`)
        if (response === undefined) return
        return response.data
    }

    async createForecasts(waypoints: Array<Array<Float32Array>>, departureTime: number): Promise<Array<Forecast>> {
        return (await this.axios.post<Array<Forecast>>(
            "/api/v1/forecasts", {
                waypoints: waypoints,
                mode: "driving",
                departure_time: departureTime
            }
        )).data
    }

    async getEvents(): Promise<Array<Event>> {
        return (await this.axios.get<Array<Event>>("/api/v1/events")).data
    }

    async createEvent(eventData: Event): Promise<Event> {
        return (await this.axios.post<Event>(
            "/api/v1/events",
            eventData
        )).data
    }

    async getCameras(page: string): Promise<Array<Camera>> {
        console.log(await this.axios.get<Array<Camera>>(`/api/v1/cameras/${page}`))
        return (await this.axios.get<Array<Camera>>(`/api/v1/cameras/${page}`)).data
    }

    async getTrafficAnalysis(waypoints: Array<Waypoint>): Promise<TrafficAnalysis> {
        return (await this.axios.post<TrafficAnalysis>(
            "/api/v1/traffic-analysis",
            waypoints
        )).data
    }

    async getTrafficLights(): Promise<Array<TrafficLight>> {
        return (await this.axios.get<Array<TrafficLight>>("/api/v1/traffic-lights")).data
    }

    async editTrafficLightState(trafficLightId: string, newState: string): Promise<number> {
        const response = await this.axios.put(
            `/api/v1/traffic-lights/${trafficLightId}`, {
                new_state: newState
            }
        )
        return response.status
    }

    async getNotifications(): Promise<Array<Notification>> {
        return (await this.axios.get<Array<Notification>>("/api/v1/notifications")).data
    }
}
