<script setup>
import { reactive } from 'vue'
import services from '../../services'
import router from '../../router'

const state = reactive({
  hasError: false,
  filters: []
})

const LABELS = {
  all: 'Todos',
  issue: 'Problemas',
  idea: 'Ideias',
  other: 'Outros'
}

const COLORS = {
  all: { text: 'text-brand-info', bg: 'bg-brand-info' },
  issue: { text: 'text-brand-danger', bg: 'bg-brand-danger' },
  idea: { text: 'text-brand-warning', bg: 'bg-brand-warning' },
  other: { text: 'text-brand-graydark', bg: 'bg-brand-graydark' }
}

function transformFiltersStructure(filters) {
  return filters.map(filter => {
    const key = filter.type.toLowerCase()
    return {
      type: filter.type,
      label: LABELS[key],
      color: COLORS[key],
      count: filter.count,
      active: key === 'all'
    }
  })
}

try {
  const { data } = await services.feedbacks.getFiltersData()
  state.filters = transformFiltersStructure(data)
} catch (err) {
  state.hasError = !!err
}

function checkIfFilterIsActive(type) {
  const filter = state.filters.find(filter => filter.type === type)
  return filter.count === 0 && filter.label !== LABELS.all
}

function handleSelect(type) {
  if (checkIfFilterIsActive(type)) return

  state.filters = state.filters.map((filter) => {
    // refact this to my own implementation
    if (filter.type === type) {
      return { ...filter, active: true }
    }
    return { ...filter, active: false }
  })

  router.push({ query: { type } })

}


</script>

<template>
  <div class="min-w-[266px]">
    <h2 class="text-2xl font-medium mb-4">Filtros</h2>
    <div class="space-y-1">
      <div v-for="filter in state.filters" :key="filter.label" @click="handleSelect(filter.type)"
           class="rounded px-4 py-1 flex items-center justify-between"
           :class="[
             { 'bg-gray-200 bg-opacity-50': filter.active },
             checkIfFilterIsActive(filter.type) ? 'cursor-not-allowed' : 'cursor-pointer hover:opacity-70'
           ]"
      >
        <div class="flex items-center space-x-2">
          <span class="w-[5px] h-[5px] rounded-full" :class="[filter.color.text, filter.color.bg]"></span>
          <span class="font-medium text-sm">
            {{ filter.label }}
          </span>
        </div>
        <span class="font-bold" :class="filter.active ? filter.color.text : 'text-brand-graydark'">
          {{ filter.count }}
        </span>
      </div>
    </div>
  </div>
</template>
