<template>
  <div>
    <teleport to="body">
      <div
        v-if="state.isActive"
        class="fixed top-0 left-0 z-50 flex items-center justify-center w-full h-full bg-black bg-opacity-50"
        @click="handleModalToogle({ status: false })"
      >
        <div class="fixed mx-10" :class="state.width" @click.stop>
          <div
            class="flex flex-col overflow-hidden bg-white rounded-lg animate__animated animate__fadeInRight animate__faster"
          >
            <div class="flex flex-col px-12 py-10 bg-white">
              <component :is="state.component" :props="state.props" :width="state.width" />
            </div>
          </div>
        </div>
      </div>
    </teleport>
  </div>
</template>

<script>
import { defineAsyncComponent, onBeforeUnmount, onMounted, reactive } from 'vue'
import useModal from '@/composables/useModal'

const DEFAULT_WIDTH = 'w-3/4 lg:w-1/3'

export default {
  components: {
    ModalLogin: defineAsyncComponent(() => import('../ModalLogin')),
    ModalCreateAccount: defineAsyncComponent(() => import('../ModalCreateAccount'))
  },

  setup() {
    const state = reactive({
      component: null,
      isActive: false,
      props: {},
      width: DEFAULT_WIDTH
    })

    const modal = useModal()

    onMounted(() => {
      modal.listen(handleModalToogle)
    })

    onBeforeUnmount(() => {
      modal.off(handleModalToogle)
    })

    const handleModalToogle = (payload) => {
      state.isActive = payload.status
      if (payload.status) {
        state.component = payload.component
        state.props = payload.props
        state.width = payload.width || DEFAULT_WIDTH
      } else {
        state.component = null
        state.props = {}
        state.width = DEFAULT_WIDTH
      }
    }

    return {
      state,
      handleModalToogle
    }
  }
}
</script>

<style lang="scss" scoped></style>
