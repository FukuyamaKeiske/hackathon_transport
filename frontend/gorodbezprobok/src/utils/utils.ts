export const getTimePeriods = (today: Date): Map<string, Date> => {
    return new Map()
        .set("day", new Date(today.getFullYear(), today.getMonth(), today.getDate()))
        .set("week", new Date(today.setDate(today.getDate() - today.getDay())))
        .set("month", new Date(today.getFullYear(), today.getMonth(), 1))
}

