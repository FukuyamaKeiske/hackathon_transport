export interface AuthActionsContextType {
    signUp: (email: string, password: string) => Promise<number>
    signIn: (email: string, password: string) => Promise<boolean>
}
