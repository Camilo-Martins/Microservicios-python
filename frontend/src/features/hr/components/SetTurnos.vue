<script setup>
import { ref, onMounted, reactive, computed } from 'vue';
import { useObtenerPersonalActivo, } from '../composables/usePersonalActivo'
import { useAsignarPersonal } from '../composables/useHorario';
import useToast from '@/stores/useToast';

const props = defineProps({
  items: {
    type: Object,
    required: true
  },

})


const { sendData: getPersonal, data: dataPersonal, loading: loadingPersonal, error: errorPersonal } = useObtenerPersonalActivo()
const { sendData, data, loading, error} = useAsignarPersonal()
const emit = defineEmits(['horarioData'])
let personalList = ref([]);
const { trigger } = useToast()

const fetchEmployees = async () => {
  await getPersonal();
  personalList.value = dataPersonal.value
  console.log(personalList.value)
};

onMounted(() => {
  fetchEmployees();
});


const selectedEmpleadoPorDia = reactive({})
const horarioID = computed(() => props.items.horario.id)

const onSelectEmpleado = async (dia) =>{
  console.log(dia, selectedEmpleadoPorDia[dia],  )
  let personal = selectedEmpleadoPorDia[dia]
  let id = horarioID.value 
   try {
        await sendData(id,
            {
               dia, personal
            })


        emit('created');

    } catch (error) {
        trigger(error)
    }

}



</script>

<template>
  <div>
      <h5 class="text-center py-4 font-bold">{{ items.horario?.nombre }}</h5>
  </div>
  <div class="max-h-96 overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
  

    <table class="min-w-full border-collapse text-center">
      <thead class="bg-slate-100 text-slate-600">
        <tr>

          <th class="px-4 py-3 ">Dias</th>
          <th class="px-4 py-3 ">Personal</th>
          <th class="px-4 py-3 ">Lista Personnal</th>

        </tr>
      </thead>
      <tbody>

        <tr v-for="(dia, index) in items?.horario?.dias" :key="dia.id" class="  border-t hover:bg-slate-200">
          <td class=" text-left px-4 py-3">{{ dia.dia_nombre }} </td>
          <td>
            <select
               v-model="selectedEmpleadoPorDia[dia.id]"
               @change="onSelectEmpleado(dia.id)">
              <option class="text-center" value="">Seleccionar personal</option>

              <option v-for="emp in personalList" :key="emp.id" :value="emp.id" >
                {{ emp.nombre_completo }} — {{ emp.rol? emp.rol : "Sin Rol"  }}
              </option>
            </select>
          </td>
          <td class="px-4 py-3 text-center"></td>


        </tr>

      </tbody>

    </table>
  </div>
</template>


<style scoped></style>
