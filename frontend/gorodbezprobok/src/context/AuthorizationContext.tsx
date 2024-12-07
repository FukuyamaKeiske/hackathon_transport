import { createContext, useEffect, useState, FC } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContextType } from '../types/authContextType';

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

const AuthorizationProvider: FC<{ children: React.ReactNode }> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
    const navigate = useNavigate();

    useEffect(() => {
        setIsAuthenticated(true)
        // const token = localStorage.getItem('token');
        // if (token) {
        //     // доделать
        //     setIsAuthenticated(true);
        // } else {
        //     navigate('/login');
        // }
    }, [navigate]);

    return (
        <AuthContext.Provider value={{isAuthenticated}}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthorizationProvider