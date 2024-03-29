import axios from 'axios'
import router from '../router'
import AuthService from './auth'
import UsersService from './users'
import FeedbacksService from './feedbacks'

import { setGlobalLoading } from '../store/global'

const API_ENVS = {
  local: 'http://localhost:8000'
}

const httpClient = axios.create({
  baseURL: API_ENVS.local,
  headers: {
    'Content-Type': 'application/json',
  }
})

httpClient.interceptors.request.use(config => {
  setGlobalLoading(true)
  const token = localStorage.getItem('token')
  if(token){
    config.headers['Authorization'] = `Bearer ${token}`
  }
  return config
})

httpClient.interceptors.response.use(
  response => {
    setGlobalLoading(false)
    return response
  },
  (error) => {
    setGlobalLoading(false)
    let canThrow = error.status === 0 || error.status === 500
    if (canThrow) {
      throw new Error(error)
    }

    if(error.status === 401){
      router.push({ name: 'Home' })
    }

    return error
  }
)

export default {
  auth: AuthService(httpClient),
  users: UsersService(httpClient),
  feedbacks: FeedbacksService(httpClient)
}
