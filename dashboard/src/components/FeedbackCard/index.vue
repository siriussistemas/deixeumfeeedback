<script setup>
import { ptBR } from 'date-fns/locale/pt-BR'
import { formatDistanceToNow } from 'date-fns'
import Badge from './Badge.vue'

import { reactive } from "vue"

const props = defineProps({
  feedback: Object,
  isOpened: {
    required: false,
    default: false
  }
})

const state = reactive({
  isClosing: false,
  isOpen: props.isOpened
})


async function handleToggleOpen() {
  state.isClosing = true

  await new Promise(resolve => {
    setTimeout(resolve, 200)
  })

  state.isOpen = true
  state.isClosing = false
}

</script>

<template>
  <div class="py-4 px-6 space-y-4 bg-gray-50 rounded">
    <header class="flex items-center justify-between">
      <badge :type="feedback.type" />
      <time class="text-sm text-gray-500 font-regular" :datetime="new Date(feedback.created_at).toISOString()">
        {{ formatDistanceToNow(new Date(feedback.created_at), { locale: ptBR, addSuffix: true }) }}
      </time>
    </header>

    <strong class="block font-medium text-lg">
      {{ feedback.text }}
    </strong>

    <div v-if="state.isOpen" class="grid grid-cols-2 gap-4 animate__animated animate__fadeInUp animate__faster" :class="{
      animate__fadeOutUp: state.isClosing
    }">
      <div class="flex flex-col">
        <p class="uppercase text-xs font-bold text-gray-500">página</p>
        <a class="font-medium text-sm">{{ feedback.page }}</a>
      </div>
      <div class="flex flex-col">
        <p class="uppercase text-xs font-bold text-gray-500">Usuário</p>
        <p class="font-medium text-sm truncate max-w-xs" :title="feedback.fingersprint">{{ feedback.fingersprint }}</p>
      </div>
      <div class="flex flex-col">
        <p class="uppercase text-xs font-bold text-gray-500">dispositivo</p>
        <p class="font-medium text-sm">{{ feedback.device }}</p>
      </div>
    </div>

    <div v-if="!state.isOpen" class="flex justify-end">
      <button class="underline text-sm" @click="handleToggleOpen">Ver detalhes</button>
    </div>
  </div>
</template>
