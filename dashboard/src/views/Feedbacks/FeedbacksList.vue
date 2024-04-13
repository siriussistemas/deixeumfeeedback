<script setup>
import { ptBR } from 'date-fns/locale/pt-BR'
import { formatDistanceToNow } from 'date-fns'
import Badge from '../../components/FeedbackCard/Badge.vue';

defineProps({
  feedbacks: Array,
})

</script>
<template>
  <!-- SPLIT THIS COMPONENT FeedbackCard in a separe component -->
  <div v-for="feedback in feedbacks" :key="feedback.id" class="py-4 px-6 space-y-4 bg-gray-50 rounded">
    <header class="flex items-center justify-between">
      <badge :type="feedback.type" />
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
        <a class="font-medium text-sm">{{ feedback.page }}</a>
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
