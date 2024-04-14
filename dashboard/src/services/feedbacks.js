const defaultPagination = {
    limit: 5,
    offset: 0
}

export default httpClient => ({
    getFeedbacks: async ({ type, limit, offset, search } = defaultPagination) => {
        const query = { limit, offset, search }

        if (type && type != 'ALL') {
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
