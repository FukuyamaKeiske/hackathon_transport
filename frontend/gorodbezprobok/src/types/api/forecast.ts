export interface Forecast {
    id: string
    timestamp: Date
    location: string
    predicted_density: number
    predicted_speed: Float32Array
}