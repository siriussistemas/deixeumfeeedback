export default httpClient => ({

    // this is a workaround to pass optional args in EC6 javascript 
    // is util because i dont need declare getFeedbacks({}) in only call getFeedback()
    // and if i need pass some params i declare this object getFeedbacks({type: 'idea'})
    // reference: https://flexiple.com/javascript/optional-parameter-javascript
    getFeedbacks: async ({type = null} = {}) => {
        let url = '/feedbacks/'

        if(type && type != 'ALL'){
            url += `?type=${type}`
        }

        const response = await httpClient.get(url)
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