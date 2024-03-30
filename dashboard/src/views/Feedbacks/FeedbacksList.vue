<script setup>
import { ptBR } from 'date-fns/locale/pt-BR'
import { formatDistanceToNow } from 'date-fns'

defineProps({
  feedbacks: Array,
})

function getFilterTypeColorAndText(type) {
  switch (type) {
    case "ISSUE":
      return {
        color: "bg-red-500",
        text: "Problemas"
      }
    case "IDEA":
      return {
        color: "bg-green-500",
        text: "Ideias"
      }
    case "OTHER":
      return {
        color: "bg-blue-500",
        text: "Outros"
      }
    default:
      return {
        color: "bg-gray-500",
        text: "Todos"
      }
  }
}

</script>
<template>
<div 
    v-for="feedback in feedbacks" :key="feedback.id"
    class="py-4 px-6 space-y-4 bg-gray-50 rounded"
  >
  <header class="flex items-center justify-between">
    <span class="px-2 py-1 font-black rounded-full text-xs text-white uppercase"
        :class="getFilterTypeColorAndText(feedback.type).color">
        {{ feedback.type }}
    </span>
    <time class="text-sm text-gray-500 font-regular" :datetime="new Date(feedback.created_at).toISOString()">
        {{ formatDistanceToNow(new Date(feedback.created_at), { locale: ptBR, addSuffix: true }) }}
    </time>
  </header>

  <strong class="block font-medium text-lg">
    {{ feedback.text }}
  </strong>
  <div class="grid grid-cols-2">
    <div class="flex flex-col">
        <p class="uppercase text-xs font-bold text-gray-500">página</p>
        <a class="font-medium text-sm">{{ feedback.type }}</a>
    </div>
    <div class="flex flex-col">
        <p class="uppercase text-xs font-bold text-gray-500">Usuário</p>
        <p class="font-medium text-sm truncate max-w-xs">{{ feedback.fingersprint }}</p>
    </div>
  </div>
  <div class="flex flex-col">
    <p class="uppercase text-xs font-bold text-gray-500">dispositivo</p>
    <p class="font-medium text-sm">{{ feedback.device }}</p>
  </div>
</div>
</template>