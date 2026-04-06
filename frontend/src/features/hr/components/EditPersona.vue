<script setup>
const props = defineProps({
  personal: {
    type: Object,
    required: true,
  },
})

import { Field } from 'vee-validate'
import { ref, watch } from 'vue'
import BaseButton from '@/components/BaseButton.vue'
import { useEditPersonal } from '../composables/useEditPersonal'
import { useRoute, useRouter } from 'vue-router'
import useToast from '@/stores/useToast'

const { sendData } = useEditPersonal()

const route = useRoute()
const router = useRouter()
const id = route.params.id
const { trigger } = useToast()

const form = ref({
  nombre_completo: '',
  rut: '',
  rol: '',
  telefono: '',
  pago_diario: '',
  medio_pago: '',
})
const emit = defineEmits(['created'])

watch(
  () => props.personal,
  (personal) => {
    if (!personal) {
      console.log('No hay props')
      return
    }

    form.value = {
      nombre_completo: personal.empleado?.nombre_completo,
      rut: personal.empleado?.rut,
      rol: personal.empleado?.rol,
      telefono: personal.empleado?.telefono,
      pago_diario: personal.empleado?.pago_diario,
      medio_pago: personal.empleado?.medio_pago,
    }
  },
  { immediate: true },
)

const submit = async () => {
  console.log(form.value)
  try {
    await sendData(id, {
      nombre_completo: form.value.nombre_completo,
      telefono: form.value.telefono,
      rut: form.value.rut ? form.value.rut : '',
      rol: form.value.rol,
      pago_diario: form.value.pago_diario,
      medio_pago: form.value.medio_pago,
    })

    emit('created')
    setTimeout(() => {
      router.push('/panel/personal')
    }, 1000)
  } catch (error) {
    console.log(error)
    trigger("El telefono o Rut ya se encuentra registrado")
  }
}
</script>

<template>
  <!-- Formulario -->
  <div class="max-w-md mx-auto bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
    <form @submit.prevent="submit" class="grid grid-cols-1 md:grid-cols-1 gap-4 items-end">
      <div class="form-field">
        <div class="pb-3"><label class="form.label">Nombre</label>:</div>

        <Field
          type="text"
          name="nombre_completo"
          class="form-input"
          v-model="form.nombre_completo"
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
          v-model="form.rut"
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
          v-model="form.telefono"
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
          v-model="form.pago_diario"
          placeholder="Ej: $20.000"
        />
      </div>

      <BaseButton label="Editar" type="submit"> Editar </BaseButton>
    </form>
  </div>
</template>

<style scoped></style>
