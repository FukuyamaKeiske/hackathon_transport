// import { createContext, useEffect, useState, FC, useMemo } from 'react';
// import { useNavigate } from 'react-router-dom';
// import { Http } from '../utils/http';
// import { FunctionalActionsContextType } from '../types/functionalActionsContextType';

// export const FunctionalActionsContext = createContext<FunctionalActionsContextType | undefined>(undefined)

// const AuthorizationProvider: FC<{ children: React.ReactNode }> = ({ children }) => {
//     // const navigate = useNavigate();
    
//     const getNotifications = async () => {
        
//     }

//     const actions = useMemo(
//         () => ({getNotifications}),
//         [getNotifications]
//     )

//     return (
//         <FunctionalActionsContext.Provider value={actions}>
//             {children}
//         </FunctionalActionsContext.Provider>
//     );
// };

// export default AuthorizationProvider