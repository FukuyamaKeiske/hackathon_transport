import { FC, useState } from "react";
import { CamerasProps } from "../props/camerasProps";

const CameraComponent: FC<CamerasProps> = ({camerasData}) => {
    const [isFocused, setIsFocused] = useState(false);

    const onFocusHandler = () => {
        setIsFocused(true);
    }

    const onBlurHandler = () => {
        setIsFocused(false);
    }

    return (
        <div className="panel__cameras__camera" onMouseEnter={onFocusHandler} onMouseLeave={onBlurHandler} tabIndex={0}>
            <b>{camerasData.name}</b><br/><br/>
            {camerasData.description}<br/>
            {camerasData.geo}
            {isFocused && (
                <iframe
                    className={`camera-iframe ${isFocused ? 'fade-in' : 'fade-out'}`} 
                    src={camerasData.live_url}
                    title="Camera"
                ></iframe>
            )}
        </div>
    )
}

export default CameraComponent