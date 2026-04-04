<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import { ref, onMounted, watch } from 'vue'
import useToast from '@/stores/useToast'
import BaseButton from '@/components/BaseButton.vue'
import { useGetNota, useAddNota } from '@/features/notas/composables'
const { trigger } = useToast()
const { sendData, data, loading, error } = useGetNota()

const {
  sendData: sendAddNota,
  data: dataAddNota,
  loading: loadingAddNota,
  error: errorAddnota,
} = useAddNota()

let notasList = ref({})
let nombre_nota = ref('')
let observaciones = ref('')

const getNota = async () => {
  await sendData()

  console.log(data.value)
  notasList.value = data.value.data
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
    trigger(error)
  }
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

              <Field
                type="text"
                name="nombre_nota"
                class="form-input"
                v-model="nombre_nota"
                placeholder="Ej: Llamar a María"
              />
            </div>

            <div class="form-field md:col-span-4">
              <div class="pb-3">
                <label class="form.label">Observaciones</label>
              </div>

              <Field
                type="text"
                name="observaciones"
                class="form-input"
                v-model="observaciones"
                placeholder="María tiene las llaves de la bodega!"
              />
            </div>

            <BaseButton label="Agregar Personal" type="submit"> Agregar </BaseButton>
          </Form>
        </div>
      </div>
    </div>

    <!-- Info -->
    <span
      class="text-blue-800 px-5 font-medium bg-blue-200 rounded-xl shadow-sm border border-blue-800 py-2 my-5"
    >
      Puede editar una nota haciendo doble clic sobre cualquier fila de la tabla!</span
    >
    <br />
    <br />
    <!-- Tabla de Notas -->

    <div class="max-h-96 overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
      <table
        class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200"
      >
        <thead class="bg-slate-100 text-slate-600">
          <tr>
            <th class="px-4 py-3 text-left" colspan="2">Nombre</th>
            <th class="px-4 py-3 text-center" colspan="8">Detalle</th>

            <th class="px-4 py-3 text-center" colspan="2">Estado</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="nota in notasList" :key="nota.id" class="border-t hover:bg-slate-200">
            <td class="px-4 py-3 text-left" colspan="2">{{ nota.nombre_nota }}</td>
            <td class="px-4 py-3 text-left" colspan="8">{{ nota.observaciones }}</td>

            <td class="px-4 py-3 text-center" colspan="2">
              <button
                :class="
                  nota.is_active
                    ? 'px-3 py-1 text-sm rounded bg-green-100 text-green-700 hover:bg-green-200'
                    : 'px-3 py-1 text-sm rounded bg-red-100 text-red-700 hover:bg-red-200'
                "
              >
                {{ nota.is_active ? 'Activo' : 'Inactivo' }}
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<style scoped></style>
