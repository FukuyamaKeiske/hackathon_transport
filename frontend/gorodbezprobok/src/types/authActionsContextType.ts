export interface AuthActionsContextType {
    login: (token: string) => void
    logout: () => void
}
