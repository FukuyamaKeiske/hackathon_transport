import { createContext, useEffect, useState, FC, useMemo } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContextType } from '../types/authContextType';
import { AuthActionsContextType } from '../types/authActionsContextType';
import { Http } from '../utils/http';

export const AuthContext = createContext<AuthContextType | undefined>(undefined)
export const AuthActionsContext = createContext<AuthActionsContextType | undefined>(undefined)

const AuthorizationProvider: FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false)
    const navigate = useNavigate();
    const http = new Http()

    const signUp = async (email: string, password: string) => {
        const status = await http.signUp(email, password);
        return status
    }

    const signIn = async (email: string, password: string) => {
        const response = await http.signIn(email, password);
        if (response !== undefined) return true
        return false
    }

    useEffect(() => {
        setIsAuthenticated(true)
        // const token = localStorage.getItem('token');
        // if (token) {
        //     setIsAuthenticated(true);
        // } else {
        //     navigate('/login');
        // }
    }, [navigate]);

    const values = useMemo(() => ({isAuthenticated}), [isAuthenticated])
    const actions = useMemo(
        () => ({signIn, signUp}),
        [signIn, signUp]
    )

    return (
        <AuthContext.Provider value={values}>
            <AuthActionsContext.Provider value={actions}>
                {children}
            </AuthActionsContext.Provider>
        </AuthContext.Provider>
    );
};

export default AuthorizationProvider