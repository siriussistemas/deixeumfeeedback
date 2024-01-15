<template>
  <div class="flex items-center justify-between w-4/5 max-w-6xl py-10">
    <div class="w-28 lg:w-36">
      <img class="w-full" src="../../assets/images/logo_white.png" alt="logo" />
    </div>
    <div class="flex">
      <ul class="flex list-none">
        <li
          @click="() => router.push({ name: 'Credentials' })"
          class="px-6 py-2 mr-2 font-bold text-white roundend-full cursor-pointer focus:outline-none"
        >
          Credenciais
        </li>
        <li
          @click="() => router.push({ name: 'Feedbacks' })"
          class="px-6 py-2 mr-2 font-bold text-white rounded-full cursor-pointer focus:outline-none"
        >
          Feedbacks
        </li>
        <li
          @click="logout"
          class="px-6 py-2 font-bold text-brand-main bg-white rounded-full cursor-pointer focus:outline-none"
        >
          {{ logoutLabel }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import useStore from '@/composables/useStore'
import { computed } from 'vue'
export default {
  setup() {
    const router = useRouter()
    const store = useStore('user');

    const logoutLabel = computed(() => {
      if(store.currentUser.name){
        return '...'
      }
      return `${store.currentUser.username} (sair)` 
    })

    const logout = () => {
      window.localStorage.removeItem('token');
      router.push({
        name: 'Home'
      })
    }

    return { router, logoutLabel, logout }
  }
}
</script>

<style lang="scss" scoped></style>
