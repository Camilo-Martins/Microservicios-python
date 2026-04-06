<script setup>
import {computed } from 'vue'
import { useAsignarPersonal, useDesasignarPersonal } from '../composables/useHorario'
import useToast from '@/stores/useToast'

const props = defineProps({
  personallist: {
    type: Array,
    required: true,
  },
  items: {
    type: Object,
    required: true,
  },
})

const { sendData: eliminarPersonal } = useDesasignarPersonal()
const { sendData } = useAsignarPersonal()

const emit = defineEmits(['horarioData', 'addPersonal', 'deletePersonal', 'persona-data'])

const { trigger } = useToast()
const horarioID = computed(() => props.items.horario.id)

const onSelectEmpleado = async (dia, empleadoID) => {
  let personal = empleadoID
  let id = horarioID.value

  if (personal == '' || personal == 'Seleccionar') {
    trigger('Seleccione personal')
  }

  try {
    await sendData(id, {
      dia,
      personal,
    })

    emit('addPersonal')
  } catch (error) {
    trigger('El Personal seleccionado ya está asignado')
  }
}

const onEliminarEmpleado = async (dia, personal) => {
  let id = horarioID.value

  console.log(id, personal, dia)

  try {
    await eliminarPersonal(id, {
      dia,
      personal,
    })

    emit('deletePersonal')
  } catch (error) {
    trigger('El personal ya fue eliminado.')
  }
}

</script>

<template>
  <div class="max-h-96 overflow-y-auto rounded-xl shadow-sm border border-slate-200">
    <div>
      <h5 class="text-center py-4 font-bold">{{ items.horario?.nombre? items.horario?.nombre: "Por favor genere un horario" }}</h5>
    </div>
    <table
      class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200"
    >
      <thead class="bg-slate-100 text-slate-600">
        <tr>
          <th class="px-4 py-3 text-left w-32">Día</th>
          <th class="px-4 py-3 text-center w-60">Asignar personal</th>
          <th class="px-4 py-3 text-center">Personal asignado</th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="dia in items?.horario?.dias"
          :key="dia.id"
          class="border-t hover:bg-slate-50 transition"
        >
          <!-- Día -->
          <td class="px-4 py-3 font-medium text-slate-700 align-top">
            {{ dia.dia_nombre }}
          </td>

          <!-- Selector compacto -->
          <td class="px-4 py-3 align-top">
            <select
              @change="onSelectEmpleado(dia.id, $event.target.value)"
              class="w-48 rounded border border-slate-300 bg-white px-2 py-1 text-sm focus:outline-none focus:ring-2 focus:ring-slate-400"
            >
              <option value="Seleccionar">Seleccionar</option>
              <option
                v-for="emp in personallist.filter((e) => e.is_active)"
                :key="emp.id"
                :value="emp.id"
              >
                {{ emp.nombre_completo }}
              </option>
            </select>
          </td>

          <!-- Personal asignado (espacio libre) -->
          <td class="px-4 py-3">
            <div class="flex flex-wrap gap-2">
              <div
                v-for="asig in dia.asignaciones"
                :key="asig.id"
                class="flex items-center gap-2 rounded-full bg-slate-200 px-3 py-1 text-sm"
              >
                <span class="text-slate-700">
                  {{ asig.empleado.nombre_completo }}
                </span>
              
                <button
                  class="text-red-600 hover:text-red-800 font-bold transition"
                  @click="onEliminarEmpleado(dia.id, asig?.empleado?.id)"
                >
                  ×
                </button>
              </div>

              <span v-if="dia.asignaciones.length === 0" class="text-slate-400 italic text-sm">
                Sin asignaciones
              </span>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
