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
          <feedback-filter :feedbacks-filters="FiltersDataWithColors" :on-filter="setFilter" :filter-type-active="filterTypeActive" />
          
          <div class="flex-1">
            <div class="space-y-6">
              <div v-for="feedback in state.feedbacks" :key="feedback.id" class="py-4 px-6 space-y-4 bg-gray-50 rounded">
                <header class="flex items-center justify-between">
                  <span class="px-2 py-1 font-black rounded-full text-xs text-white uppercase"
                    :class="getFilterTypeColorAndText(feedback.type).color" 
                  >
                    {{ feedback.type }}
                  </span>
                  <time class="text-sm text-gray-500 font-regular" datetime="">
                    {{ formatDistanceToNow(new Date(feedback.created_at), {locale: ptBR, addSuffix: true}) }}
                  </time>
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
import { reactive, watchEffect, computed } from "vue";
import { useRoute, useRouter } from 'vue-router';

import { ptBR } from 'date-fns/locale/pt-BR'
import { formatDistanceToNow } from 'date-fns'

const router = useRouter()
const route = useRoute()

const state = reactive({
  isLoading: false,
  hasError: false,
  feedbacks: [],
  filtersData: []
}) 

const filterTypeActive = computed(() => {
  return route.query.type || 'ALL'
})

// move to another file
const validFilters = ["ALL", "ISSUE", "IDEA", "OTHER"]

// move to another file
function getFilterTypeColorAndText(type){
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

const FiltersDataWithColors = computed(() => {
  return state.filtersData.map(filter => {
    return {
      ...filter,
      ...getFilterTypeColorAndText(filter.type)
    };
  });
});

// TODO: merge the two functions in one to avoid code duplication

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
    const response = await services.feedbacks.filterByType(type)
    state.feedbacks = response.data
}

async function fetchFiltersData(){
  const response = await services.feedbacks.getFiltersData()
  state.filtersData = response.data
}


function setFilter(type) {
  if (validFilters.includes(type)) {
    router.push({ query: { type } })
  }
}

watchEffect(async () => {
  const type = route.query.type
  if (type && validFilters.includes(type)) {
    // TODO: remove this else
    if (type === "ALL") {
      fetchFeedbacks()
    } else {
      fetchFeedbacksByType(type)
    }
  }
})

fetchFeedbacks()
fetchFiltersData()

</script>
