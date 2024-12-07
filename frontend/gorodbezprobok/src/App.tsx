import { FC } from "react"
import {Route, Routes, BrowserRouter } from "react-router-dom"
import AuthorizationProvider from "./context/AuthorizationContext"
import AuthorizationPage from "./pages/AuthorizationPage"
import PanelPage from "./pages/PanelPage"
import MapPage from "./pages/MapPage"

const App: FC = () => {
  
  return (
    <BrowserRouter>
      <AuthorizationProvider>
        <Routes>
            <Route path="/login" element={<AuthorizationPage />}/>
            <Route path="/" element={<PanelPage />}/>
            <Route path="/map" element={<MapPage />}/>
        </Routes>
      </AuthorizationProvider>
    </BrowserRouter>
  )
}
export default App
