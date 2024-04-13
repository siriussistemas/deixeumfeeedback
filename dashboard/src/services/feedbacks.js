const defaultPagination = {
    limit: 5,
    offset: 0
}

export default httpClient => ({
    getFeedbacks: async ({ type, limit, offset } = defaultPagination) => {
        console.log(type, limit, offset)

        const query = { limit, offset }

        if (type) {
            query.type = type
        }

        const response = await httpClient.get('/feedbacks', { params: query })
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
