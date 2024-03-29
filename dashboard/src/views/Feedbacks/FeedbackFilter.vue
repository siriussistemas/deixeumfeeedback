<script setup>
defineProps({
  onFilter: Function,
  feedbacksFilters: Array
})

</script>

<template>
<div class="min-w-[266px]">
  <h2 class="text-2xl font-medium mb-4">Filtros</h2>
  <div class="space-y-1">
    <div 
      v-for="filterOption in feedbacksFilters" 
      :key="filterOption.id"
      @click="onFilter(filterOption.id)"
      class="hover:bg-gray-100 rounded px-4 py-1 flex items-center justify-between"
    >
    <div class="flex items-center space-x-2">
      <span class="w-1 h-1 bg-blue-500 rounded-full"></span>
      <span class="font-medium text-sm">{{ filterOption.text }}</span>
    </div>
    <span class="font-black text-sm text-[#8296FB] opacity-70">200</span>
    </div>
  </div>
</div>
</template>