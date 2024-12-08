export interface FunctionalActionsContextType {
    getNotifications: () => Promise<Array<Notification>>
}