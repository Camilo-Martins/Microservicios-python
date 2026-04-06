<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import BaseButton from '@/components/BaseButton.vue'
import useToast from '@/stores/useToast'
import { useAddProveedor } from '../composables/composables'
import { proveedorSchema } from '../schemas/proveedorSchema'

const { trigger } = useToast()
const { sendData } = useAddProveedor()
const emit = defineEmits(['created'])

const submit = async (values, { resetForm }) => {
  try {
    await sendData({
      nombre_completo: values.nombre_completo,
      telefono: values.telefono,
      rut: values.rut,
      email: values.email,
      nombre_empresa: values.nombre_empresa,
      direccion: values.direccion,
      observaciones: values.observaciones,
    })

    resetForm()
    emit('created')
  } catch (error) {
    trigger('El telefono o email ya existe, por favor ingrese uno diferente.', 'error')
  }
}
</script>

<template>
  <!-- Formulario -->
  <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
    <Form :validation-schema="proveedorSchema" @submit="submit" 
    class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
      <div class="form-field col-span-12">
        <div class="pb-3"><label class="form.label">Representante:</label></div>

        <Field type="text" name="nombre_completo" 
        class="form-input" placeholder="Ej: Camilo Álvarez" />
      </div>

      <div class="form-field col-span-8">
        <div class="pb-3">
          <label class="form.label">Telefono:</label>
        </div>

        <Field type="text" name="telefono" class="form-input" placeholder="Ej: 912345678" />
      </div>

      <div class="form-field col-span-4">
        <div class="pb-3">
          <label class="form.label">Nombre Empresa:</label>
        </div>

        <Field type="text" name="nombre_empresa" class="form-input" placeholder="Nombre de la Empresa" />
      </div>

      <div class="form-field col-span-8">
        <div class="pb-3">
          <label class="form.label">Rut:</label>
        </div>

        <Field type="text" name="rut" class="form-input" placeholder="112345678-9" />
      </div>

      <div class="form-field col-span-4">
        <div class="pb-3">
          <label class="form.label">Email:</label>
        </div>

        <Field type="text" name="email" class="form-input" placeholder="ejemplo@dominio.com" />
      </div>

      <div class="form-field col-span-12">
        <div class="pb-3">
          <label class="form.label">Observaciones:</label>
        </div>

        <Field type="text" name="observaciones" class="form-input" placeholder="Solo reparte los lunes" />
      </div>
      <ErrorMessage name="nombre_completo" class="text-red-600 col-span-12 italic" />
      <ErrorMessage name="telefono" class="text-red-600 col-span-12 italic" />
      <ErrorMessage name="nombre_empresa" class="text-red-600 col-span-12 italic" />
      <BaseButton class="col-span-12" label="Agregar Personal" type="submit"> Agregar </BaseButton>
    </Form>
  </div>
</template>
<style scoped></style>
