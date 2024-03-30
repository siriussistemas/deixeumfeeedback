<script setup>
import ContentLoader from "@/components/ContentLoader"

const props = defineProps({
  total: {
    type: Number,
    default: 3
  }
})

const totalFeedbacksFakeArray = new Array(props.total).fill(0)

</script>
<template>
<div 
  class="py-4 px-6 space-y-4 bg-gray-50 rounded"
  v-for="index in totalFeedbacksFakeArray"
  :key="index"
  >
  <header class="flex items-center justify-between">
    <ContentLoader width="4.5rem" class="rounded" /> <ContentLoader 
      width="4.5rem" 
      class="rounded"
    />
  </header>

  <ContentLoader 
    width="100%"
    class="rounded"
  />
                
  <div class="grid grid-cols-2">
    <div class="flex flex-col">
      <ContentLoader 
        width="420px"
        class="rounded"
      />
    </div>
  </div>
  <div class="flex flex-col">
    <ContentLoader 
      width="453px"
      class="rounded"
    />
  </div>
</div>
</template>