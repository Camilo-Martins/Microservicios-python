<script setup>
import { Form, Field } from 'vee-validate'
import { ref, onMounted } from 'vue'
import useToast from '@/stores/useToast'
import BaseButton from '@/components/BaseButton.vue'
import { useGetNota, useAddNota, useEditNota } from '@/features/notas/composables/composables'

const { trigger } = useToast()

const { sendData, data, loading, error } = useGetNota()
const editing = ref({
  id: null,
  field: null,
  value: '',
})

const { sendData: sendAddNota } = useAddNota()

const { sendData: sendEditNota } = useEditNota()

let notasList = ref({})
let nombre_nota = ref('')
let observaciones = ref('')
let showHelp = ref(false)

const getNota = async () => {
  await sendData()
  notasList.value = data.value.data
}

const startEdit = (nota, field) => {
  editing.value.id = nota.id
  editing.value.field = field
  editing.value.value = nota[field] ?? ''
}

const cancelEdit = () => {
  editing.value.id = null
  editing.value.field = null
  editing.value.value = ''
}

const saveEdit = async (nota) => {
  const { field, value } = editing.value

  if (!field) return

  if (value === nota[field]) {
    cancelEdit()
    return
  }

  const confirmed = window.confirm('¿Guardar cambios?')
  if (!confirmed) {
    cancelEdit()
    return
  }

  try {
    await sendEditNota(nota.id, {
      [field]: value,
    })

    nota[field] = value
    getNota()
  } catch (error) {
  } finally {
    cancelEdit()
  }
}

const submit = async () => {
  try {
    await sendAddNota({
      nombre_nota: nombre_nota.value,
      observaciones: observaciones.value,
    })

    nombre_nota.value = ''
    observaciones.value = ''
    getNota()
  } catch (error) {
    trigger('Debe ingresar un nombre para la nota')
  }
}

const toggleEstado = async (nota) => {
  const nuevoEstado = !nota.is_active

  const confirmed = window.confirm(
    `¿Deseas marcar esta nota como ${nuevoEstado ? 'Activa' : 'Inactiva'}?`,
  )
  if (!confirmed) return

  try {
    await sendEditNota(nota.id, {
      is_active: nuevoEstado,
    })

    nota.is_active = nuevoEstado
    getNota()
  } catch (error) { }
}

onMounted(() => {
  getNota()
})
</script>

<template>
  <section class="w-full px-6 py-6">
    <header class="mb-6">
      <h1 class="text-2xl font-semibold text-slate-800 uppercase">Agrega Recordatorios</h1>
      <p class="text-sm text-slate-500">Y no olvides tus tareas importantes!!</p>
    </header>

    <!-- Agregar una nota -->
    <div class="grid grid-cols-12">
      <div class="col-span-12">
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
          <Form @submit="submit()" class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
            <div class="form-field md:col-span-2">
              <div class="pb-3"><label class="form.label">Nombre</label>:</div>

              <Field type="text" name="nombre_nota" class="form-input" v-model="nombre_nota"
                placeholder="Ej: Llamar a María" />
            </div>

            <div class="form-field md:col-span-4">
              <div class="pb-3">
                <label class="form.label">Observaciones</label>
              </div>

              <Field type="text" name="observaciones" class="form-input" v-model="observaciones"
                placeholder="María tiene las llaves de la bodega!" />
            </div>

            <BaseButton label="Agregar Personal" type="submit"> Agregar </BaseButton>
          </Form>
        </div>
      </div>
    </div>

    <div class="max-h-96 overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
      <table
        class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
        <thead class="bg-slate-100 text-slate-600">
          <tr>
            <th class="px-4 py-3 text-left" colspan="1">Nombre</th>
            <th class="px-4 py-3 text-left" colspan="11">Detalle</th>
            <th class="px-4 py-3 text-center" colspan="1">Estado</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="nota in notasList" :key="nota.id" class="border-t hover:bg-slate-200"
            title="Haz doble clic para editar" :class="[
              editing.id === nota.id ? 'bg-blue-100 ring-1 ring-blue-400' : 'hover:bg-slate-200',
            ]">
            <!-- NOMBRE -->
            <td class="px-4 py-3 text-left truncate max-w-xs" colspan="1">
              <input v-if="editing.id === nota.id && editing.field === 'nombre_nota'" v-model="editing.value"
                type="text" class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(nota)"
                @keyup.enter="saveEdit(nota)" @keyup.esc="cancelEdit" />

              <span v-else class="block w-full cursor-pointer" @click="startEdit(nota, 'nombre_nota')">
                {{ nota.nombre_nota }}
              </span>
            </td>

            <!-- OBSERVACIONES -->
            <td class="px-4 py-3 text-left truncate max-w-xs" colspan="10">
              <textarea v-if="editing.id === nota.id && editing.field === 'observaciones'" v-model="editing.value"
                rows="3" class="w-full rounded border border-slate-300 px-2 py-1 resize-none" @blur="saveEdit(nota)"
                @keyup.esc="cancelEdit"></textarea>

              <span v-else class="block w-full cursor-pointer whitespace-pre-line"
                @click="startEdit(nota, 'observaciones')">
                {{ nota.observaciones ? nota.observaciones : 'Sin detalles' }}
              </span>
            </td>

            <!-- ESTADO -->
            <td class="px-4 py-3 text-center" colspan="2">
              <button @click="toggleEstado(nota)" :class="nota.is_active
                  ? 'px-3 py-1 text-sm rounded bg-green-100 text-green-700 hover:bg-green-200'
                  : 'px-3 py-1 text-sm rounded bg-red-100 text-red-700 hover:bg-red-200'
                ">
                {{ nota.is_active ? 'Realizada' : 'Pendiente' }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<style scoped></style>
