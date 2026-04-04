<script setup>
import { ref, onMounted } from 'vue'
import { useGetPersona } from '../composables/useGetPersona'
import { useRoute, useRouter } from 'vue-router'
import EditPersona from '../components/EditPersona.vue'

const {
  sendData: getPersona,
  data: dataPersona,
  loading: loadingPersona,
  error: errorPersona,
} = useGetPersona()
const route = useRoute()
const id = route.params.id
let personaData = ref([])

onMounted(() => {
  fetchEmploye()
})

const fetchEmploye = async () => {
  await getPersona(id)
  personaData.value = dataPersona.value

  if (errorPersona == true) {
    window.location.href = `/panel/personal`
  }
  //personalList.valuae = dataPersonal.value
}
</script>

<template>
  <p v-if="loadingPersona" class="rounded-md bg-slate-100 px-3 py-2 text-sm text-center">
    Cargando perfil...
  </p>

  <p
    v-else-if="errorPersona"
    class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-800 text-center font-bold uppercase"
  >
    Redirigiendo
  </p>

  <div v-else>
    <EditPersona :personal="personaData" />
  </div>
</template>

<style scoped></style>
