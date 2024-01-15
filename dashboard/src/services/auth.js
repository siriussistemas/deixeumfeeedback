export default (httpClient) => {
  return {
    login: async ({ email, password }) => {
      const response = await httpClient.post('/auth/login/', {
        email,
        password
      })
      let errors = null

      if (!response.data) {
        errors = {
          status: response.request.status,
          statusText: response.request.statusText
        }
      }

      return {
        data: response.data,
        errors
      }
    },
    register: async ({ email, password, name }) => {
      const response = await httpClient.post('/auth/register/', { email, password, username: name })
      let errors = null
      if (!response.data) {
        errors = {
          status: response.request.status,
          statusText: response.request.statusText
        }
      }

      return {
        data: response.data,
        errors
      }
    }
  }
}
