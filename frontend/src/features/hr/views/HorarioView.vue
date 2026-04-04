<script setup>
import { ref, onMounted } from 'vue'
import AddHorario from '../components/AddHorario.vue'
import SetTurnos from '../components/SetTurnos.vue'
import { useGetHorario } from '../composables/useHorario'

let horarioData = ref({})

const {
  sendData: getHorario,
  data: dataHorario,
} = useGetHorario()

const fetchHorario = async () => {
  await getHorario()
  horarioData.value = dataHorario.value
  console.log(horarioData.value)
}

onMounted(() => {
  fetchHorario()
})
</script>

<template>
  <section class="w-full px-6 py-6">
    <!-- Header -->
    <header class="mb-6">
      <h1 class="text-2xl font-semibold text-slate-800 uppercase">Horario</h1>
      <p class="text-sm text-slate-500">Crea un horario y asigna personal a tu medida</p>
    </header>

    <AddHorario @created="fetchHorario" />
    <SetTurnos :items="horarioData" @addPersonal="fetchHorario" @deletePersonal="fetchHorario" />
  </section>
</template>

<style scoped></style>
