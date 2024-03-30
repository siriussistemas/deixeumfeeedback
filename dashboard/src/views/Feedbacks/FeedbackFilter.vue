<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';

defineProps({
  onFilter: Function,
  feedbacksFilters: Array,
  filterTypeActive: String
})

const route = useRoute()

const filterTypeActive = computed(() => {
  return route.query.type || 'ALL'
})

</script>

<template>
<div class="min-w-[266px]">
  <h2 class="text-2xl font-medium mb-4">Filtros</h2>
  <div class="space-y-1">
    <div 
      v-for="filterOption in feedbacksFilters" 
      :key="filterOption.id"
      @click="onFilter(filterOption.type)"
      class="rounded px-4 py-1 flex items-center justify-between"
      :class="{'bg-gray-100': filterOption.type === filterTypeActive}"
    >
    <div class="flex items-center space-x-2">
      <span class="w-[5px] h-[5px] rounded-full"
        :class="filterOption.color"
        >
      </span>
      <span class="font-medium text-sm">{{ filterOption.text }}</span>
    </div>
    <span class="font-black text-sm opacity-70">{{ filterOption.count }}</span>
    </div>
  </div>
</div>
</template>