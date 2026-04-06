<script setup>
import { computed, ref } from 'vue'
import { useEditProveedor } from '../composables/composables'
import useToast from '@/stores/useToast'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const props = defineProps({
  proveedoreslist: {
    type: Array,
    required: true,
  },
})

const editing = ref({
  id: null,
  field: null,
  value: '',
})

const emit = defineEmits(['updatedProveedor'])
const { trigger } = useToast()
const { sendData } = useEditProveedor()
const startEdit = (proveedor, field) => {
  editing.value.id = proveedor.id
  editing.value.field = field
  editing.value.value = proveedor[field] ?? ''
}

const cancelEdit = () => {
  editing.value.id = null
  editing.value.field = null
  editing.value.value = ''
}

const saveEdit = async (proveedor) => {
  const { field, value } = editing.value

  if (!field) return

  if (value === proveedor[field]) {
    cancelEdit()
    return
  }

  const confirmed = window.confirm('¿Guardar cambios?')
  if (!confirmed) {
    cancelEdit()
    return
  }

  try {
    await sendData(proveedor.id, {
      [field]: value,
    })

    emit('updatedProveedor')
    proveedor[field] = value
  } catch (error) {
    trigger(error.data.rut)
  } finally {
    cancelEdit()
  }
}

const toggleEstado = async (proveedor) => {
  const nuevoEstado = !proveedor.is_active

  const confirmed = window.confirm(
    `¿Deseas marcar esta nota como ${nuevoEstado ? 'Activa' : 'Inactiva'}?`,
  )
  if (!confirmed) return

  try {
    await sendData(proveedor.id, {
      is_active: nuevoEstado,
    })

    proveedor.is_active = nuevoEstado
    emit('updatedProveedor')
  } catch (error) {
    console.log(error.value)
    trigger("Error al actualizar proveedor")
   }
}
</script>

<template>
  <div class="max-h-96 overflow-y-auto rounded-xl shadow-sm border border-slate-200">
    <table
      class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
      <thead class="bg-slate-100 text-slate-600">
        <tr>
          <th class="px-4 py-3 text-left" colspan="1">Nombre</th>
          <th class="px-4 py-3 text-center" colspan="1">Rut</th>
          <th class="px-4 py-3 text-center" colspan="1">Telefono</th>
          <th class="px-4 py-3 text-center" colspan="1">Email</th>
          <th class="px-4 py-3 text-center" colspan="1">Nombre Empresa</th>
          <th class="px-4 py-3 text-center" colspan="6">Observaciones</th>
          <th class="px-4 py-3 text-center" colspan="1">Estado</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="proveedor in proveedoreslist" :key="proveedor.id"
          class="border-t hover:bg-slate-50 transition cursor-pointer hover:bg-slate-200"
          title="Haz doble clic para editar" :class="[
            editing.id === proveedor.id ? 'bg-blue-100 ring-1 ring-blue-400' : 'hover:bg-slate-200',
          ]">
          <!-- Nombre -->
          <td class="px-4 py-3 text-left truncate max-w-xs" colspan="1">
            <input v-if="editing.id === proveedor.id && editing.field === 'nombre_completo'" v-model="editing.value"
              type="text" class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(proveedor)"
              @keyup.enter="saveEdit(proveedor)" @keyup.esc="cancelEdit" />

            <span v-else class="block w-full cursor-pointer" @click="startEdit(proveedor, 'nombre_completo')">
              {{ proveedor.nombre_completo ? proveedor.nombre_completo : 'No definido' }}
            </span>
          </td>

          <!-- Rut -->
          <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
            <input v-if="editing.id === proveedor.id && editing.field === 'rut'" v-model="editing.value" type="text"
              class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(proveedor)"
              @keyup.enter="saveEdit(proveedor)" @keyup.esc="cancelEdit" />

            <span v-else class="block w-full cursor-pointer" @click="startEdit(proveedor, 'rut')">
              {{ proveedor.rut ? proveedor.rut : 'No definido' }}
            </span>
          </td>

          <!-- Telefono -->
          <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
            <input v-if="editing.id === proveedor.id && editing.field === 'telefono'" v-model="editing.value"
              type="text" class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(proveedor)"
              @keyup.enter="saveEdit(proveedor)" @keyup.esc="cancelEdit" />


              
            <span v-else class="block w-full cursor-pointer" @click="startEdit(proveedor, 'telefono')" >
              +{{ proveedor.telefono ? proveedor.telefono : 'No definido' }}
            </span>
          </td>

          <!-- Email -->
          <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
            <input v-if="editing.id === proveedor.id && editing.field === 'email'" v-model="editing.value" type="text"
              class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(proveedor)"
              @keyup.enter="saveEdit(proveedor)" @keyup.esc="cancelEdit" />

            <span v-else class="block w-full cursor-pointer" @click="startEdit(proveedor, 'email')">
              {{ proveedor.email ? proveedor.email : 'No definido' }}
            </span>
          </td>

          <!-- Nombre Empresa -->
          <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
            <input v-if="editing.id === proveedor.id && editing.field === 'nombre_empresa'" v-model="editing.value"
              type="text" class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(proveedor)"
              @keyup.enter="saveEdit(proveedor)" @keyup.esc="cancelEdit" />

            <span v-else class="block w-full cursor-pointer" @click="startEdit(proveedor, 'nombre_empresa')">
              {{ proveedor.nombre_empresa ? proveedor.nombre_empresa : 'No definido' }}
            </span>
          </td>

          <!-- Observaciones -->
          <td class="px-4 py-3 text-center truncate max-w-xs" colspan="6">
            <input v-if="editing.id === proveedor.id && editing.field === 'observaciones'" v-model="editing.value"
              type="text" class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(proveedor)"
              @keyup.enter="saveEdit(proveedor)" @keyup.esc="cancelEdit" />

            <span v-else class="block w-full cursor-pointer" @click="startEdit(proveedor, 'observaciones')">
              {{ proveedor.observaciones ? proveedor.observaciones : 'No definido' }}
            </span>
          </td>

          <!-- Productos -->

          <td class="px-4 py-3 text-center" colspan="1">
            <button @click="toggleEstado(proveedor)" :class="proveedor.is_active
                ? 'px-3 py-1 text-sm rounded bg-green-100 text-green-700 hover:bg-green-200'
                : 'px-3 py-1 text-sm rounded bg-red-100 text-red-700 hover:bg-red-200'
              ">
              {{ proveedor.is_active ? 'Activo' : 'Inactivo' }}
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<style scoped></style>
