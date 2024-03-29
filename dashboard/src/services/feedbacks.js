export default httpClient => ({
    getFeedbacks: async () => {
        const response = await httpClient.get("/feedbacks")
        return {
            data: response.data
        }
    },
    filterByType: async (type) => {
        const response = await httpClient.get(`/feedbacks/?type=${type}`)
        return {
            data: response.data
        }
    },

    getFiltersData: async () => {
        const response = await httpClient.get('/feedbacks/filters_data')
        return {
            data: response.data
        }
    }
})