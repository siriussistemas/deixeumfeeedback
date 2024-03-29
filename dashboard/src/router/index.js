import { createRouter, createWebHistory } from 'vue-router'

import services from '../services'
import { setCurrentUser } from '../store/user'

const Home = () => import('../views/Home')
const Feedbacks = () => import('../views/Feedbacks')
const Credentials = () => import('../views/Credentials')

const router = createRouter({
  history: createWebHistory('/'),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/feedbacks',
      name: 'Feedbacks',
      component: Feedbacks,
      meta: {
        hasAuth: true
      }
    },
    {
      path: '/credentials',
      name: 'Credentials',
      component: Credentials,
      meta: {
        hasAuth: true
      }
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: {
        name: 'Home'
      }
    }
  ]
})


async function isAuthenticated(){
  try {
    const token = window.localStorage.getItem('token')

    if (!token){
      return false
    }

    const { data } = await services.users.getMe();
    setCurrentUser(data)

  } catch {
    return false
  }

  return true
}

router.beforeEach(async (to) => {
  if(to.meta.hasAuth && !isAuthenticated()){
    return {
      name: "Login"
    }
  }
})



export default router
