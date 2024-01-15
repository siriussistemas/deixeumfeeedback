<template>
      <component :is="props.name" />
</template>

<script>
import Loading from './Loading.vue';
import Copy from './Copy.vue';

export default {
  components: {
    Loading,
    Copy,
  },

  props: {
    name: {
      type: String,
      required: true
    }
  },
  setup (props) {
    

    return {
      props
    }
  }
}
</script>

<style lang="scss" scoped>

</style>