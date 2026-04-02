<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import { ref } from 'vue'
import { useAddPersonal } from '../composables/useAddPersonal'
import BaseButton from '@/components/BaseButton.vue'

import useToast from '@/stores/useToast'
import { useAddHorario } from '../composables/useHorario'

const { trigger } = useToast()

const { sendData, loading, error } = useAddPersonal()

let rol = ref('')
let nombre_completo = ref('')
let telefono = ref('')
let medio_pago = ref('')
let pago_diario = ref('')
let rut = ref('')

const emit = defineEmits(['created', 'generated'])
const { sendData: sendHorario, error: errorHorario, data } = useAddHorario()

const submitHorario = async () => {
  console.log('!')
  try {
    await sendHorario()

    emit('generated')
  } catch (error) {
    trigger(errorHorario)
  }
}

const submit = async () => {
  try {
    await sendData({
      nombre_completo: nombre_completo.value,
      telefono: telefono.value,
      rut: rut.value,
      rol: rol.value,
      pago_diario: pago_diario.value,
      medio_pago: medio_pago.value,
    })

    emit('created')
  } catch (error) {
    trigger(error)
  }
}
</script>

<template>
  <!-- Formulario -->
  <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
    <Form @submit="submit()" class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
      <div class="form-field">
        <div class="pb-3"><label class="form.label">Nombre</label>:</div>

        <Field
          type="text"
          name="nombre_completo"
          class="form-input"
          v-model="nombre_completo"
          placeholder="Ej: Camilo Álvarez"
        />
      </div>

      <div class="form-field">
        <div class="pb-3">
          <label class="form.label">RUT</label>
        </div>

        <Field
          type="text"
          name="rut"
          class="form-input"
          v-model="rut"
          placeholder="Ej:12345678-9"
        />
      </div>

      <div class="form-field">
        <div class="pb-3">
          <label class="form.label">Telefono</label>
        </div>

        <Field
          type="text"
          name="telefono"
          class="form-input"
          v-model="telefono"
          placeholder="56912345678"
        />
      </div>

      <div class="form-field">
        <div class="py-3">
          <label class="form.label">Monto Pago</label>
        </div>
        <Field
          type="text"
          name="pago_diario"
          class="form-input"
          v-model="pago_diario"
          placeholder="Ej: $20.000"
        />
      </div>

      <BaseButton label="Agregar Personal" type="submit"> Agregar </BaseButton>
      <BaseButton
        label="Generar Horario"
        class="bg-green-800 hover:bg-green-900"
        type="button"
        @click="submitHorario"
      >
        Generar Horario
      </BaseButton>
    </Form>
  </div>
</template>

<style scoped></style>
