import { useContext } from "react";
import { FunctionalActionsContext } from "../context/AuthorizationContext";

export const useFunctionalActions = () => {
    const context = useContext(FunctionalActionsContext);
    if (!context) {
        throw new Error('useFunctionalActions must be used within an AuthProvider');
    }
    return context;
}