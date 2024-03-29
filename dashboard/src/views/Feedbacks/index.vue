<template>
  <div class="flex justify-center w-full h-28 bg-brand-main">
    <header-logged />
  </div>

  <div class="flex flex-col items-center justify-center h-64 bg-brand-gray">
    <h1 class="text-5xl font-black text-center text-gray-800">Feedbacks</h1>
    <p class="text-2xl text-center text-gray-800 font-regular">
      Detalhes de todos os feedbacks recebidos
    </p>
  </div>

  <div class="flex justify-center w-full h-full">
    <div class="flex flex-col w-4/5 max-w-6xl py-10">
        <h1 class="mb-9 text-3xl font-black text-brand-darkgray">Listagem</h1>

        <div class="flex gap-16">
          <feedback-filter :feedbacks-filters="feedbacksFilters" :on-filter="setFilter" />
          
          <div class="flex-1">
            <div class="space-y-6">
              <div v-for="feedback in state.feedbacks" :key="feedback.id" class="py-4 px-6 space-y-4 bg-gray-50 rounded">
                <header class="flex items-center justify-between">
                  <span class="px-2 py-1 font-black rounded-full bg-red-400 text-xs text-white uppercase">
                    {{ feedback.type }}
                  </span>
                  <time class="text-sm text-gray-500 font-regular" datetime="">20 segundos atrás</time>
                </header>

                <strong class="block font-medium text-lg">
                  {{ feedback.text }}
                </strong>
                
                <div class="grid grid-cols-2">
                  <div class="flex flex-col">
                    <p class="uppercase text-xs font-bold text-gray-500">página</p>
                    <a class="font-medium text-sm" >{{ feedback.type }}</a>
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
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import HeaderLogged from '@/components/HeaderLogged'
import FeedbackFilter from './FeedbackFilter.vue';

import services from "../../services"
import { reactive, watchEffect } from "vue";
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()

const state = reactive({
  isLoading: false,
  hasError: false,
  feedbacks: [],
}) 

const feedbacksFilters = [
  {
    id: "ALL",
    text: "Todos",
    color: ""
  },
  {
    id: "ISSUE",
    text: "Problemas",
    color: ""
  },
  {
    id: "IDEA",
    text: "Ideias",
    color: ""
  },
  {
    id: "OTHER",
    text: "Outros",
    color: ""
  }
]

const validFilters = feedbacksFilters.map(filter => filter.id)

async function fetchFeedbacks() {
  state.isLoading = true
  try {
    const response = await services.feedbacks.getFeedbacks()
    state.feedbacks = response.data
  } catch (error) {
    console.error(error)
    state.hasError = true
  } finally {
    state.isLoading = false
  }
}

async function fetchFeedbacksByType(type) {
  state.isLoading = true
  try {
    const response = await services.feedbacks.filterByType(type)
    state.feedbacks = response.data
  } catch (error) {
    console.error(error)
    state.hasError = true
  } finally {
    state.isLoading = false
  }
}

fetchFeedbacks()

function setFilter(type) {
  if (validFilters.includes(type)) {
    setQuery(type)
  }
}

function setQuery(type) {
  router.push({ query: { type } })
}

function cleanQuery() {
  router.push({ query: {} })
}

watchEffect(async () => {
  const type = route.query.type
  if (type && validFilters.includes(type)) {
    if (type === "ALL") {
      fetchFeedbacks()
    } else {
      fetchFeedbacksByType(type)
    }
    cleanQuery()
  }
})


</script>
