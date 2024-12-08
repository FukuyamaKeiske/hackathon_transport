export const getTimePeriods = (today: Date): Map<string, number> => {
    return new Map()
        .set("day", new Date(today.getFullYear(), today.getMonth(), today.getDate()).getTime())
        .set("week", new Date(today.getFullYear(), today.getMonth(), today.getDate() - 7).getTime())
        .set("month", new Date(today.getFullYear(), today.getMonth(), 1).getTime())
}

