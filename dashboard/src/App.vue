<template>
  <ModalFactory />
  <RouterView />
</template>

<script>
import ModalFactory from './components/ModalFactory'
import { onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { setCurrentUser } from '@/store/user'
import services from '@/services'

export default {
  components: {
    ModalFactory
  },
  setup() {
    const route = useRoute()
    const router = useRouter()

    watch(
      () => route.path,
      async () => {
        if (route.meta.hasAuth) {
          const token = window.localStorage.getItem('token')
          if (!token) {
            router.push({
              name: 'Home'
            })
          }

          const { data } = await services.users.getMe();
          setCurrentUser(data)
        }
      }
    )
  }
}
</script>

<style scoped></style>
