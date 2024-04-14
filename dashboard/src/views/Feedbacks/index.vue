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
    <div class="flex flex-col px-4 sm:w-4/5 sm:px-0 max-w-6xl py-10">
      <div class="flex flex-col sm:flex-row gap-2 mb-6 sm:gap-0 sm:mb-8">
        <h1 class="text-3xl font-black text-brand-darkgray">Listagem</h1>

        <div class="relative z-0 flex justify-end flex-1 items-center sm:px-2">
          <div class="w-full sm:max-w-md">
            <label htmlFor="search" class="sr-only">
              Busque
            </label>
            <div class="relative">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                <!-- TODO: Put this icon -->
                <!-- <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" aria-hidden="true" /> -->
              </div>
              <input id="search" name="search" v-model="state.searchText"
                class="block w-full rounded-md border-0 bg-gray-50 py-1.5 pl-10 pr-3 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Busque por um feedback" type="search" />
            </div>
          </div>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row gap-16">

        <Suspense>
          <feedback-filter />
          <template #fallback>
            <feedback-filter-loader />
          </template>
        </Suspense>

        <div class="flex-1 flex flex-col items-center">
          <div class="space-y-6">

            <div class="font-bold pt-8 text-gray-800" v-if="!state.isLoading && state.hasError">
              Ocorreu um erro ao carregar seus feedbacks!😓<br>
              Se esse persistir entre em contato com o suporte!
            </div>

            <div class="font-bold pt-8 text-gray-800"
              v-else-if="!state.isLoading && !state.hasError && state.feedbacks.length === 0">
              Parece que você não tem nenhum feedback ainda! 😵
            </div>

            <feedbacks-list v-else :feedbacks="state.feedbacks" />

            <feedback-loader v-if="state.isLoading" :total="5" />
            <!-- Handle error state -->
            <feedback-loader v-if="state.isLoadingMoreFeedbacks" :total="3" />
          </div>
          <button class="px-4 py-1.5 rounded my-6 text-center bg-gray-50 border font-medium hover:bg-gray-100"
            v-if="state.pagination.total != state.feedbacks.length" @click="handleLoadMoreFeedbacks">
            Carregar mais feedbacks
          </button>
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
import { reactive, watch } from "vue";
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()

const state = reactive({
  isLoading: false,
  isLoadingMoreFeedbacks: false,
  isFilterDataLoading: false, // remove this
  hasError: false,
  feedbacks: [],
  searchText: '',
  filtersData: [],
  pagination: {
    limit: 5,
    offset: 0,
    total: 0
  },
})

function handleErrors(error) {
  state.isLoading = false
  state.isLoadingMoreFeedbacks = false
  state.hasError = !!error
}

async function fetchFeedbacks({ type, search }) {
  try {
    state.isLoading = true
    state.pagination.offset = 0
    state.pagination.limit = 5

    const { data } = await services.feedbacks.getFeedbacks({
      ...state.pagination,
      type,
      search
    })

    console.log(data.results[0].type)
    state.feedbacks = data.results

    if (data.next) {
      const query = data.next.split('?')[1]
      const paginationNextParams = new URLSearchParams(query)

      const offset = Number(paginationNextParams.get("offset"))
      const limit = Number(paginationNextParams.get("limit"))

      state.pagination = { ...state.pagination, limit, offset }
    }

    state.pagination = { ...state.pagination, total: data.count }
    state.isLoading = false

  } catch (error) {
    console.error(error)
    handleErrors(error)
  }
}

async function handleSearchFeedback({ search }) {
  router.push({ query: { ...route.query, search } })
}

async function handleLoadMoreFeedbacks() {
  try {
    // state.isLoading = true
    state.isLoadingMoreFeedbacks = true

    const { data } = await services.feedbacks.getFeedbacks({
      ...state.pagination,
      ...route.query
    })

    if (data.results.length) {
      state.feedbacks.push(...data.results)
    }

    if (data.next) {
      const query = data.next.split('?')[1]
      const paginationNextParams = new URLSearchParams(query)

      const offset = Number(paginationNextParams.get("offset"))
      const limit = Number(paginationNextParams.get("limit"))

      state.pagination = { limit, offset, total: data.count }
    }

    state.pagination = { ...state.pagination, total: data.count }
    state.isLoadingMoreFeedbacks = false

  } catch (error) {
    console.error(error)
    handleErrors(error)
  }
}

watch(() => state.searchText, async (searchText) => {
  await handleSearchFeedback({ search: searchText })
})

watch(() => route.query, async (query, oldQuery) => {
  if (query.type != oldQuery.type)
    await fetchFeedbacks({ type: query.type })
  if (query.seach != oldQuery.search)
    await fetchFeedbacks({ ...query, search: query.search })
})


fetchFeedbacks({})
router.push({ query: {} })

</script>
