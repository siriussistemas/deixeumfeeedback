<template>
  <div class="flex justify-between">
    <h1 class="text-4xl font-black text-gray-800">Entre na sua conta</h1>

    <button class="text-4xl text-gray-600" @click="close">&times;</button>
  </div>
  <div class="mt-16">
    <form @submit.prevent="handleSubmit">
      <label class="block">
        <span class="text-lg font-medium text-gray-800">Email</span>
        <input
          v-model="state.email.value"
          type="email"
          placeholder="jhondoe@gmail.com"
          class="block w-full px-4 py-3 mt-1 text-lg bg-gray-100 border-2 rounded outline-none"
          :class="{ 'border-brand-danger': !!state.email.errorMessage }"
          required
        />
        <span class="block font-medium text-brand-danger">
          {{ state.email.errorMessage }}
        </span>
      </label>
      <label class="block my-3">
        <span class="text-lg font-medium text-gray-800">Senha</span>
        <input
          v-model="state.password.value"
          type="password"
          class="block w-full px-4 py-3 mt-1 text-lg bg-gray-100 border-2 rounded outline-none"
          :class="{ 'border-brand-danger': !!state.password.errorMessage }"
          required
        />
        <span class="block font-medium text-brand-danger">
          {{ state.password.errorMessage }}
        </span>
      </label>

      <button
        :disabled="state.isLoading"
        type="submit"
        :class="{ 'opacity-50': state.isLoading }"
        class="w-full px-8 py-3 mt-1 text-2xl font-bold text-center text-white rounded bg-brand-main transition-all duration-150"
      >
        <Icon v-if="state.isLoading" class="inline-block animate-spin" name="Loading" />
        <span v-else>Entrar</span>
      </button>
    </form>
  </div>
</template>

<script>
import { reactive } from 'vue'
import { useField } from 'vee-validate'
import { useToast } from 'vue-toastification'
import useModal from '../../composables/useModal'

import { validateEmptyAndLength3, validateEmail } from '../../utils/validators'

import Icon from '../Icon'

import services from '@/services'
import { useRouter } from 'vue-router'

export default {
  components: {
    Icon
  },

  setup() {
    const { value: emailValue, errorMessage: emailErrorMessage } = useField('email', [
      validateEmptyAndLength3,
      validateEmail
    ])
    const { value: passwordValue, errorMessage: passwordErrorMessage } = useField(
      'password',
      validateEmptyAndLength3
    )

    const state = reactive({
      isLoading: false,
      hasErrors: false,
      email: {
        value: emailValue,
        errorMessage: emailErrorMessage
      },
      password: {
        value: passwordValue,
        errorMessage: passwordErrorMessage
      }
    })

    const router = useRouter()
    const toast = useToast()
    const modal = useModal()

    async function handleSubmit() {
      try {
        toast.clear()
        state.isLoading = true
        const { data, errors } = await services.auth.login({
          email: state.email.value,
          password: state.password.value
        })

        if (!errors) {
          window.localStorage.setItem('token', data.access)
          router.push({
            name: 'Feedbacks'
          })
          modal.close()
          return
        }

        if (errors.status == 404) {
          toast.error('Usuário não encontrado')
        }
        if (errors.status == 401) {
          toast.error('E-mail/Senha inválidos')
        }
        if (errors.status == 400) {
          toast.error('Ocorreu um erro ao fazer o login')
        }
      } catch (error) {
        state.hasErrors = !!error
        toast.error('Erro ao fazer login')
      } finally {
        state.isLoading = false
      }
    }

    return {
      state,
      close: modal.close,
      handleSubmit
    }
  }
}
</script>

<style lang="scss" scoped></style>
