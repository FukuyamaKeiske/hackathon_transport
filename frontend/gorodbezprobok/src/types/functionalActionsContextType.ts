import { Notification } from "./api/notification";

export interface FunctionalActionsContextType {
    getNotifications: () => Promise<Array<Notification>>
}