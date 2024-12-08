import { FC } from "react"
import {Route, Routes, BrowserRouter } from "react-router-dom"
import AuthorizationProvider from "./context/AuthorizationContext"
import AuthorizationPage from "./pages/AuthorizationPage"
import PanelPage from "./pages/PanelPage"
import MapPage from "./pages/MapPage"
import CamerasPage from "./pages/CamerasPage"
import IncidentsPage from "./pages/IncidentsPage"
import TrafficLightsPage from "./pages/TrafficLightsPage"

const App: FC = () => {
  
  return (
    <BrowserRouter>
      <AuthorizationProvider>
        <Routes>
            <Route path="/login" element={<AuthorizationPage />}/>
            <Route path="/" element={<PanelPage />}/>
            <Route path="/map" element={<MapPage />}/>
            <Route path="/cameras/:page" element={<CamerasPage />}/>
            <Route path="/incidents" element={<IncidentsPage />}/>
            <Route path="/traffic-lights" element={<TrafficLightsPage/>}/>
        </Routes>
      </AuthorizationProvider>
    </BrowserRouter>
  )
}
export default App
