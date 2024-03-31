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

        <feedback-filter-loader v-if="state.isFilterDataLoading" />
        <feedback-filter v-else 
          :feedbacks-filters="FiltersDataWithColors" 
          :on-filter="setFilter"
          :filter-type-active="filterTypeActive" 
        />

        <div class="flex-1">
          <div class="space-y-6">

            <feedback-loader v-if="state.isLoading" 
              :total="5" 
            />
            <feedbacks-list v-else 
              :feedbacks="state.feedbacks" 
            />
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import HeaderLogged from '@/components/HeaderLogged'
import FeedbackLoader from './FeedbackLoader'
import FeedbackFilterLoader from './FeedbackFilterLoader';
import FeedbackFilter from './FeedbackFilter';
import FeedbacksList from './FeedbacksList.vue';

import services from "../../services"
import { reactive, watchEffect, computed } from "vue";
import { useRoute, useRouter } from 'vue-router';

const router = useRouter()
const route = useRoute()

const state = reactive({
  isLoading: false,
  isFilterDataLoading: false, // remove this
  hasError: false,
  feedbacks: [],
  filtersData: []
})

// TODO: Sinceramente não estou sastifeito com o resultado obtido com a filterloader tem bastante
// depedencia aqui nesse componente PAI, então é melhor levar todas a logica de loading, error para um componente separado
// para facilitar a questão da refatoração etc... separar em dois componentes um para ListaDeFeedbacks e outro para FiltroDeFeedbacks
// toda requisição de API deve tratar todos os status de uma requisição (loading, error, )

const filterTypeActive = computed(() => {
  return route.query.type || 'ALL'
})

// move to another file
const validFilters = ["ALL", "ISSUE", "IDEA", "OTHER"]

// move to another file
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

const FiltersDataWithColors = computed(() => {
  return state.filtersData.map(filter => {
    return {
      ...filter,
      ...getFilterTypeColorAndText(filter.type)
    };
  });
});

async function fetchFeedbacks({type = null} = {}) {
  state.isLoading = true
  const response = await services.feedbacks.getFeedbacks({type})
  state.feedbacks = response.data
  state.isLoading = false
}

async function fetchFiltersData() {
  state.isFilterDataLoading = true
  const response = await services.feedbacks.getFiltersData()
  state.filtersData = response.data
  state.isFilterDataLoading = false
}

function setFilter(type) {
  if (validFilters.includes(type)) {
    router.push({ query: { type } })
  }
}

watchEffect(async () => {
  const type = route.query.type
  if (type && validFilters.includes(type)) {
      fetchFeedbacks({type})
    }
  })


Promise.all([
  fetchFiltersData(),
  fetchFeedbacks(),
])

</script>
