import { useContext } from "react";
import { AuthActionsContext } from "../context/AuthorizationContext";

export const useAuthActions = () => {
    const context = useContext(AuthActionsContext);
    if (!context) {
        throw new Error('useAuthActions must be used within an AuthProvider');
    }
    return context;
}