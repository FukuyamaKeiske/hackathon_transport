import { FC } from "react";
import { format } from "date-fns"
import { NotificationProps } from "../props/notificationProps";

const Notification: FC<NotificationProps> = ({notificationData}) => {
    return (
        <div className="panel__notifications__notification">
            <b>{notificationData.title}</b><br/><br/>
            {notificationData.description}<br/>
            {format(notificationData.time, "dd.MM.yyyy")}
        </div>
    )
}

export default Notification