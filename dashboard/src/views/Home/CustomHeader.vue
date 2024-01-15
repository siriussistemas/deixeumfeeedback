<template>
  <header class="header">
    <div class="header-group">
      <div class="flex items-center justify-between py-10">
        <div class="w-28 lg:w-36">
          <img class="w-full" src="../../assets/images/logo_white.png" alt="logo" />
        </div>
        <div class="flex">
          <button
            class="px-6 p-2 font-bold rounded-full text-white focus:outline-none"
            @click="() => emit('create-account')"
          >
            Criar conta
          </button>
          <button
            class="px-6 p-2 font-bold bg-white rounded-full text-brand-main focus:outline-none"
            @click="() => emit('login')"
          >
            Entrar
          </button>
        </div>
      </div>
      
      <!-- This is the content of the header -->
      <div class="flex flex-col mt-28">
        <h1 class="text-4xl font-black text-white">
          Tenha um feedback. <br />
          E faça seus clientes mais <br class="hidden lg:inline-block" />
          felizes!
        </h1>
        <p class="text-lg font-medium text-white">
          Receba ideias, reclamações e feedbacks com um <br class="hidden lg:inline-block" />
          simples widget na página.
        </p>
        <div>
          <button
            class="mt-5 px-6 p-2 font-bold bg-white rounded-full text-brand-main focus:outline-none"
          >
            Crie uma conta grátis
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  setup(_, { emit }) {
    return { emit }
  }
}
</script>

<style lang="postcss" scoped>
.header {
  @apply bg-brand-main w-full flex justify-center;
  height: 700px;
}

.header-group {
  @apply flex flex-col w-4/5 max-w-6xl;
}

@media (min-width: 640px) {
  .header-group {
    background-image: url("../../assets/images/home_ballons.png");
    background-size: 628px;
    background-position: 90% 100%;
    background-repeat: no-repeat;
  }
}
</style>
