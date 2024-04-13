<script setup>
import { computed } from 'vue';

const props = defineProps({
  type: String
})

const typeNormalizedToLowerCase = computed(() => props.type.toLocaleLowerCase())

const LABELS = {
  issue: 'Problema',
  idea: 'Ideia',
  other: 'Outro'
}

const COLORS = {
  issue: { bg: 'bg-brand-danger' },
  idea: { bg: 'bg-brand-warning' },
  other: { bg: 'bg-brand-graydark' }
}

const badgeLabel = computed(() => LABELS[typeNormalizedToLowerCase.value])
const badgeClass = computed(() => COLORS[typeNormalizedToLowerCase.value].bg)

</script>

<template>
  <span class="px-2 py-1 font-black rounded-full text-xs text-white uppercase w-20 text-center" :class="badgeClass">
    {{ badgeLabel }}
  </span>
</template>
