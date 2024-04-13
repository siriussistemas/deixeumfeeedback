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

        <Suspense>
          <feedback-filter />
          <template #fallback>
            <feedback-filter-loader />
          </template>
        </Suspense>

        <div class="flex-1">
          <div class="space-y-6">
            <feedbacks-list v-if="!state.isLoading && !state.hasError" :feedbacks="state.feedbacks" />
            <feedback-loader v-else-if="state.isLoading" :total="5" />
            <!-- Handle empty state -->
            <!-- Handle error state -->
            <feedback-loader v-if="state.isLoadingMoreFeedbacks" :total="3" />
          </div>
          <button v-if="state.pagination.total != state.feedbacks.length" @click="handleLoadMoreFeedbacks">
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

async function fetchFeedbacks({ type }) {
  try {
    state.isLoading = true
    state.pagination.offset = 0
    state.pagination.limit = 5

    const { data } = await services.feedbacks.getFeedbacks({
      ...state.pagination,
      type
    })
    state.feedbacks = data.results

    // extract this to a function
    const query = data.next.split('?')[1]
    const paginationNextParams = new URLSearchParams(query)

    const offset = Number(paginationNextParams.get("offset"))
    const limit = Number(paginationNextParams.get("limit"))

    state.pagination = { limit, offset, total: data.count }
    state.isLoading = false

  } catch (error) {
    handleErrors(error)
  }
}

async function handleLoadMoreFeedbacks() {
  try {
    // state.isLoading = true
    state.isLoadingMoreFeedbacks = true

    const { data } = await services.feedbacks.getFeedbacks({
      ...state.pagination,
      type: route.query.type
    })

    if (data.results.length) {
      state.feedbacks.push(...data.results)
    }

    if (data.next) {

      // extract this to a function
      const query = data.next.split('?')[1]
      const paginationNextParams = new URLSearchParams(query)

      const offset = Number(paginationNextParams.get("offset"))
      const limit = Number(paginationNextParams.get("limit"))

      state.pagination = { limit, offset, total: data.count }
    }

    state.isLoadingMoreFeedbacks = false

  } catch (error) {
    console.error(error)
    handleErrors(error)
  }
}

watch(() => route.query, async (query) => {
  await fetchFeedbacks({ type: query.type })
})

fetchFeedbacks({})
router.push({ query: {} })

</script>
