<script setup>
import useToast from '@/stores/useToast'
import { useAddHorario } from '../composables/useHorario'
import {  Field } from 'vee-validate'
const { trigger } = useToast()
const { sendData } = useAddHorario()

const emit = defineEmits(['created'])

const submit = async () => {
  try {
    await sendData()

    emit('created')
  } catch (error) {
    trigger(error)
  }
}
</script>

<template>
  <!-- Formulario -->

  <form @submit.prevent="submit"  class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
     <div class="form-field">
      <div class="pb-3"><label class="form.label">Nombre</label>:</div>
 
      <Field
        type="submit"
        name="nombre_completo"
        class="form-input"
        v-model="nombre_completo"
        placeholder="Ej: Camilo Álvarez"
      />
    </div>
 
  </form>
</template>

<style scoped></style>
