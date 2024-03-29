<template>
  <div class="flex justify-center w-full h-28 bg-brand-main">
    <header-logged />
  </div>

  <div class="flex flex-col items-center justify-center h-64 bg-brand-gray">
    <h1 class="text-4xl font-black text-center text-gray-800">Credenciais</h1>
    <p class="text-lg text-center text-gray-800 font-regular">
      Guia de instalação e geração de suas credenciais
    </p>
  </div>

  <div class="flex justify-center w-full h-full">
    <div class="flex flex-col w-4/5 max-w-6xl py-10">
      <h1 class="text-3xl font-black text-brand-darkgray">Instalação e configuração</h1>

      <p class="mt-10 text-lg text-gray-800 font-regular">Este aqui é a sua chave de api</p>

      <content-loader
        v-if="store.global.isLoading || state.isLoading"
        class="rounded"
        width="600px"
        height="50px"
      />

      <div
        v-else
        class="flex py-3 pl-5 mt-2 rounded justify-between items-center bg-brand-gray w-full lg:w-1/2"
      >
        <span v-if="state.hasError">Erro ao carregar a Api key</span>
        <span v-else>{{ store.user.currentUser.api_key}}</span>

        <div class="flex ml-20 mr-5" v-if="!state.hasError">
          <icon
            @click="handleCopy"
            name="copy"
            :color="brandColors.graydark"
            size="24"
            class="cursor-pointer"
          />
          <icon
            id="generate-apikey"
            name="loading"
            :color="brandColors.graydark"
            size="24"
            class="cursor-pointer ml-3"
          />
        </div>
      </div>

      <p class="mt-5 text-lg text-gray-800 font-regular">
        Coloque o script abaixo no seu site para começar a receber feedbacks
      </p>

      <content-loader
        v-if="store.global.isLoading || state.isLoading"
        class="rounded"
        width="600px"
        height="50px"
      />
      <div
        v-else
        class="py-3 pl-5 pr-20 mt-2 rounded bg-brand-gray w-full lg:w-2/3 overflow-x-scroll"
      >
        <span v-if="state.hasError">Erro ao carregar o script</span>
        <pre v-else>
&lt;script
  defer
  async
  onload="init('{{ store.user.currentUser.apiKey }}')"
  src="https://Jackson-Vieira-feedbacker-widget.netlify.app/init.js"
&gt;&lt;/script&gt;
        </pre>
      </div>
    </div>
  </div>
</template>

<script setup>
import HeaderLogged from '@/components/HeaderLogged'
import ContentLoader from '../../components/ContentLoader'
import Icon from '../../components/Icon'

import { reactive, watch } from 'vue'
import { useToast } from 'vue-toastification'
import { setApiKey } from '../../store/user'
import useStore from '../../composables/useStore'
import services from '../../services'

const store = useStore()
const toast = useToast()
const state = reactive({
  hasError: false,
  isLoading: false
})

const brandColors = {
  main: '#EF4983',
  gray: '#F9F9F9',
  info: '#8296FB',
  graydark: '#C0BCB0',
  warning: '#E4B52E',
  danger: '#F88676'
}

function handleError(error) {
  state.isLoading = false
  state.hasError = !!error
}

async function handleCopy() {
  toast.clear()

  try {
    await navigator.clipboard.writeText("implement this")
    toast.success('API key copiada para a clipboard!')
  } catch (error) {
    handleError(error)
  }
}

async function handleGenerateNewApikey() {
  try {
    state.isLoading = true

    const { data } = await services.users.generateApikey()

    setApiKey(data.apiKey)

    state.isLoading = false
  } catch (error) {
    handleError(error)
  }
}

watch(
  () => store.user.currentUser,
  () => {
    if (!store.global.isLoading && !store.user.currentUser.api_keys) {
      handleError(true)
    }
  }
)
</script>
