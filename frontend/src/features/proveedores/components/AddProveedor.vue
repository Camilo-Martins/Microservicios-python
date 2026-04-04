<script setup>
import { Form, Field } from 'vee-validate'
import { ref } from 'vue'
import BaseButton from '@/components/BaseButton.vue'
import useToast from '@/stores/useToast'
import { useAddProveedor } from '../composables/composables'

const { trigger } = useToast()
const { sendData } = useAddProveedor()
const emit = defineEmits(['created'])

let nombre_completo = ref('')
let telefono = ref('')
let email = ref('')
let rut = ref('')
let nombre_empresa = ref('')
let direccion = ref('')
let observaciones = ref('')

const submit = async () => {
  try {
    await sendData({
      nombre_completo: nombre_completo.value,
      telefono: telefono.value,
      rut: rut.value,
      email: email.value,
      nombre_empresa: nombre_empresa.value,
      direccion: direccion.value,
      observaciones: observaciones.value,
    })

    nombre_completo.value = ''
    telefono.value = '' 
    rut.value = ''
    email.value = ''
    nombre_empresa.value = ''
    direccion.value = ''
    observaciones.value = ''
    
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
      
      <div class="form-field col-span-12">
        <div class="pb-3"><label class="form.label">Nombre</label>:</div>

        <Field
          type="text"
          name="nombre_completo"
          class="form-input"
          v-model="nombre_completo"
          placeholder="Ej: Camilo Álvarez"
        />
      </div>

      <div class="form-field col-span-8">
        <div class="pb-3">
          <label class="form.label">Telefono</label>
        </div>

        <Field
          type="text"
          name="Telefono"
          class="form-input"
          v-model="telefono"
          placeholder="Ej: 912345678"
        />
      </div>

      
      <div class="form-field col-span-4">
        <div class="pb-3">
          <label class="form.label">Nombre de la Empresa</label>
        </div>

        <Field
          type="text"
          name="nombre_empresa"
          class="form-input"
          v-model="nombre_empresa"
          placeholder="Nombre de la Empresa"
        />
      </div>

      <div class="form-field col-span-8">
        <div class="pb-3">
          <label class="form.label">Rut</label>
        </div>

        <Field type="text" name="rut" class="form-input" v-model="rut" placeholder="112345678-9" />
      </div>

      <div class="form-field col-span-4">
        <div class="pb-3">
          <label class="form.label">Email</label>
        </div>

        <Field
          type="text"
          name="email"
          class="form-input"
          v-model="email"
          placeholder="ejemplo@dominio.com"
        />
      </div>


      <div class="form-field col-span-12">
        <div class="pb-3">
          <label class="form.label">Observaciones</label>
        </div>

        <Field
          type="text"
          name="observaciones"
          class="form-input"
          v-model="observaciones"
          placeholder="Solo reparte los lunes"
        />
      </div>

      <BaseButton class="col-span-12" label="Agregar Personal" type="submit"> Agregar </BaseButton>
    </Form>
  </div>
</template>
<style scoped></style>
