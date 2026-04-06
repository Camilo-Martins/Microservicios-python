<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import { useAddPersonal } from '../composables/useAddPersonal'
import BaseButton from '@/components/BaseButton.vue'

import useToast from '@/stores/useToast'
import { useAddHorario } from '../composables/useHorario'
import { personalSchema } from '../schemas/personalSchema'
const { trigger } = useToast()

const { sendData } = useAddPersonal()

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

const submit = async (values, { resetForm }) => {
  try {
    await sendData({
      nombre_completo: values.nombre_completo,
      telefono: values.telefono,
      rut: values.rut,
      rol: values.rol,
      pago_diario: values.pago_diario,
      medio_pago: values.medio_pago,
    })

    resetForm()
    emit('created')
  } catch (error) {
    trigger("Error al agregar pesonal")
  }
}
</script>

<template>
  <!-- Formulario -->
  <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
    <Form :validation-schema="personalSchema" @submit="submit" 
    class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
      <div class="form-field">
        <div class="pb-3"><label class="form.label">Nombre</label>:</div>

        <Field
          type="text"
          name="nombre_completo"
          class="form-input"
         
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
        <div class="form-field col-span-12">
       <ErrorMessage name="nombre_completo" class="text-red-600 col-span-6 italic" />
         <ErrorMessage name="rut" class="text-red-600 col-span-6 italic" />
           <ErrorMessage name="telefono" class="text-red-600 col-span-6 italic" />
             <ErrorMessage name="pago_diario" class="text-red-600 col-span-6 italic" />
      </div>
    </Form>
    
        
  </div>
</template>

<style scoped></style>
