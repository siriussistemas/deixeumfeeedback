<template>
  <div class="flex justify-center w-full h-28 bg-brand-main">
    <header-logged />
  </div>

  <div class="flex flex-col items-center justify-center h-64 bg-brand-gray">
    <h1 class="text-5xl font-black text-center text-gray-800">Feedbacks</h1>
    <p class="text-2xl text-center text-gray-800 font-regular">
      Detalhes de todos os feedbacks recebidos
    </p>
  </div>

  <div class="flex justify-center w-full h-full">
    <div class="flex flex-col w-4/5 max-w-6xl py-10">
        <h1 class="mb-9 text-3xl font-black text-brand-darkgray">Listagem</h1>

        <div class="flex gap-16">
          <div class="min-w-[266px]">
            <h2 class="text-2xl font-medium mb-4">Filtros</h2>

            <!-- FeedbacksFilter -->
            <div class="space-y-1">
              <div class="hover:bg-gray-100 rounded px-4 py-1 flex items-center justify-between" v-for="filterOption in feedbacksFilters" :key="filterOption.type">
                <div class="flex items-center space-x-2">
                  <span class="w-1 h-1 bg-blue-500 rounded-full"></span>
                  <span class="font-medium text-sm">{{ filterOption.type }}</span>
                </div>
                <span class="font-black text-sm text-[#8296FB] opacity-70">200</span>
              </div>
            </div>

          </div>
          <div class="flex-1">
            <div class="space-y-6">
              <div v-for="feedback in new Array(10).fill(0)" :key="feedback" class="py-4 px-6 space-y-4 bg-gray-50 rounded">
                <header class="flex items-center justify-between">
                  <span class="px-2 py-1 font-black rounded-full bg-red-400 text-xs text-white uppercase">
                    problema 
                  </span>
                  <time class="text-sm text-gray-500 font-regular" datetime="">20 segundos atrás</time>
                </header>

                <strong class="block font-medium text-lg">
                  Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                  Voluptates saepe a repellat reiciendis, esse atque quo quia quisquam asperiores in?
                </strong>
                
                <div class="grid grid-cols-2">
                  <div class="flex flex-col">
                    <p class="uppercase text-xs font-bold text-gray-500">página</p>
                    <a class="font-medium text-sm" >https://deixeumfeedback.com/ajuda</a>
                  </div>
                  <div class="flex flex-col">
                    <p class="uppercase text-xs font-bold text-gray-500">Usuário</p>
                    <p class="font-medium text-sm">g0faklsdfkl</p>
                  </div>
                </div>
                <div class="flex flex-col">
                  <p class="uppercase text-xs font-bold text-gray-500">dispositivo</p>
                  <p class="font-medium text-sm">Chrome 85.0, macOS 10.14</p>
                </div>
              </div>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import HeaderLogged from '@/components/HeaderLogged'

const feedbacksFilters = [
  {
    type: "Todos",
    color: ""
  },
  {
    type: "Problemas",
    color: ""
  },
  {
    type: "Ideias",
    color: ""
  },
  {
    type: "Outros",
    color: ""
  }
]

</script>
