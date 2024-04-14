<script setup>
import FeedbackCard from '../../components/FeedbackCard/index.vue'

defineProps({
  feedbacks: Array,
})

</script>
<template>
  <feedback-card v-for="(feedback, index) in feedbacks" :key="feedback.id" :feedback="feedback"
    :is-opened="index === 0" />
</template>
