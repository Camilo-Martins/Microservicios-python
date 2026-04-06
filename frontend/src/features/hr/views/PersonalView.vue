<script setup>
import { ref, onMounted } from 'vue'

import { useObtenerPersonal } from '../composables/useObtenerPersonal'
import TablePersonal from '../components/TablePersonal.vue'
import SetTurnos from '../components/SetTurnos.vue'
import { useDeletePersonal } from '../composables/useDeletePersonal'
import AddPersonal from '../components/AddPersonal.vue'
import { useGetPersona } from '../composables/useGetPersona'
import { useGetHorario } from '../composables/useHorario'

const { sendData: getPersonal, data: dataPersonal } = useObtenerPersonal()
const { sendData: sendPersonal } = useDeletePersonal()
const { sendData: getPersona } = useGetPersona()
const { sendData: getHorario, data: dataHorario } = useGetHorario()
let horarioData = ref({})

const selectedId = ref(null)

let personalList = ref([])

const fetchEmployees = async () => {
  await getPersonal()
  personalList.value = dataPersonal.value
}

onMounted(() => {
  fetchHorario()
  fetchEmployees()
})

const toggleEmployeeStatus = async (id) => {
  await sendPersonal(id)
  await fetchEmployees()
}

const toPersona = async (id) => {
  await getPersona(id)
}

const fetchHorario = async () => {
  await getHorario()
  horarioData.value = dataHorario.value
}
</script>

<template>
  <section class="w-full px-6 py-6">
    <!-- Header -->
    <header class="mb-6">
      <h1 class="text-2xl font-semibold text-slate-800 uppercase">Personal</h1>
      <p class="text-sm text-slate-500">Gestión básica de empleados de la tienda</p>
    </header>

    <div class="grid grid-cols-12">
      <div class="col-span-12">
        <AddPersonal @created="fetchEmployees" @generated="fetchHorario" />
      </div>
    </div>

    <div class="grid grid-cols-12 gap-6">
      <div class="col-span-6">
        <TablePersonal :items="personalList" :selected-id="selectedId" @persona-data="toPersona"
          @toggle-status="toggleEmployeeStatus" />
      </div>
      <div class="col-span-6">
        <SetTurnos :items="horarioData" :personallist="personalList" @addPersonal="fetchHorario"
          @deletePersonal="fetchHorario" />
      </div>
    </div>
  </section>
</template>

<style scoped></style>
