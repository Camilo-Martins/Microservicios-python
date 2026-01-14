<script setup>
import { ref, onMounted } from 'vue';

import { useObtenerPersonal } from '../composables/useObtenerPersonal';
import TablePersonal from '../components/TablePersonal.vue';
import { useDeletePersonal } from '../composables/useDeletePersonal';
import AddPersonal from '../components/AddPersonal.vue';
import { personalSchema } from '@/features/private/schemas/personalSchema';
import { useGetPersona } from '../composables/useGetPersona';

const { sendData: getPersonal, data: dataPersonal, loading: loadingPersonal, error: errorPersonal } = useObtenerPersonal()
const { sendData: sendPersonal, data: deletedPersonal , loading: loadingDeleted, error: errorDeleted } = useDeletePersonal()
const { sendData: getPersona, data: dataPersona , loading: loadingPersona, error: errorPersona } = useGetPersona()

const selectedId = ref(null)

let personalList = ref([]);

const fetchEmployees = async () => {
    console.log("!")
    await getPersonal();
    personalList.value = dataPersonal.value
};

onMounted(() => {
    fetchEmployees();
});

const toggleEmployeeStatus = async (id) => {
    await sendPersonal(id)
    await  fetchEmployees();
};

const toPersona = async (id) => {
    await getPersona(id)
};

</script>

<template>
    <section class="w-full px-6 py-6">
        <!-- Header -->
        <header class="mb-6">
            <h1 class="text-2xl font-semibold text-slate-800 uppercase">Personal</h1>
            <p class="text-sm text-slate-500">Gestión básica de empleados de la tienda</p>
        </header>

      <AddPersonal
         @created="fetchEmployees"
      />

      <TablePersonal
        :items="personalList"
        :selected-id="selectedId"
        @persona-data="toPersona"
         @toggle-status="toggleEmployeeStatus"
      />

    </section>
</template>


<style scoped></style>
