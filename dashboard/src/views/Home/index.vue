<template>
  <CustomHeader @create-account="handleAccountCreate" @login="handleLogin" />
  <Contact />
  <div class="flex justify-center py-10 bg-brand-gray">
    <p class="font-medium text-center text-gray-800">Feedbacker © 2024</p>
  </div>
</template>
<script>
import Contact from './Contact.vue'
import CustomHeader from './CustomHeader.vue'

import { useRouter } from 'vue-router'
import useModal from '@/composables/useModal'
import { onMounted } from 'vue'

export default {
  components: {
    Contact,
    CustomHeader
  },
  setup() {
    const modal = useModal()
    const router = useRouter()

    onMounted(() => {
      if (window.localStorage.getItem('token'))
        router.push({
          name: 'Feedbacks'
        })
    })

    const handleAccountCreate = () => {
      modal.open({
        component: 'ModalCreateAccount'
      })
    }

    const handleLogin = () => {
      modal.open({
        component: 'ModalLogin'
      })
    }

    return {
      handleAccountCreate,
      handleLogin
    }
  }
}
</script>

<style lang="postcss" scoped></style>
