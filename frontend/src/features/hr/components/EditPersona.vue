<script setup>
const props = defineProps({
  personal: {
    type: Object,
    required: true
  }
})

import { Form, Field, ErrorMessage} from 'vee-validate';
import { ref, watch } from 'vue';
import { useAddPersonal } from '../composables/useAddPersonal';

import BaseButton from '@/components/BaseButton.vue';
import { personalSchema } from '@/features/private/schemas/personalSchema';
const { sendData, loading, error } = useAddPersonal()

const roles = [
    { label: 'Vendedor', value: 'Vendedor' },
    { label: 'Cajero', value: 'Cajero' },
    { label: 'Seguridad', value: 'Seguridad' },
    { label: 'Reponedor', value: 'Reponedor' },
];

const medios_pago = [
    { label: 'Transferencia', value: 'Transferencia' },
    { label: 'Efectivo', value: 'Efectivo' }
];

const form = ref({
  nombre_completo: '',
  rut: '',
  rol: '',
  telefono: '',
  pago_diario: '',
  medio_pago: ''
})
const emit = defineEmits(['created'])


watch(
  () => props.personal,
  (personal) => {
    if (!personal){
        console.log("No hay props")
        return
    } 

    
    form.value = {
      nombre_completo: personal.empleado?.nombre_completo,
      rut: personal.empleado?.rut,
      rol: personal.empleado?.rol,
      telefono: personal.empleado?.telefono,
      pago_diario: personal.empleado?.pago_diario,
      medio_pago: personal.empleado?.medio_pago
    }
  },
  { immediate: true }
)




const submit = async () => {
    await sendData(
        {
            nombre_completo: nombre_completo.value, telefono: telefono.value,
            rut: rut.value, rol: rol.value, pago_diario: pago_diario.value,
            medio_pago: medio_pago.value
        })

    
    emit('created');
   


};
</script>

<template>

    <!-- Formulario -->
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
        <form  
          
         @submit.prevent="submit"
            class="grid grid-cols-1 md:grid-cols-1 gap-4 items-end">


            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">Nombre</label>:
                </div>

                <Field type="text" name="nombre_completo" class="form-input" v-model="form.nombre_completo"
                    placeholder="Ej: Camilo Álvarez" />


            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">RUT</label>
                 
                </div>

                <Field type="text" name="rut" class="form-input" v-model="form.rut" placeholder="Ej:12345678-9" />

            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">ROL</label>
                </div>


                <select v-model="form.rol" class="form-input">
                    <option value="" disabled>Seleccionar</option>

                    <option v-for="rol in roles" :key="rol.value" :value="rol.value">
                        {{ rol.label }}
                    </option>
                </select>

            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">Telefono</label>
                
                </div>

                <Field type="text" name="telefono" class="form-input" v-model="form.telefono" placeholder="56912345678" />

            </div>

            <div class="form-field">

                <div class="py-3">
                    <label class="form.label">Monto Pago</label>
                </div>
                <Field type="text" name="pago_diario" class="form-input" v-model="form.pago_diario"
                    placeholder="Ej: $20.000" />

            </div>

            <div class="form-field">
                <div class="py-3">
                    <label class="form.label">Medio Pago</label>
                </div>

                <select v-model="form.medio_pago" class="form-input">
                    <option value="" disabled>Seleccionar</option>

                    <option v-for="mp in medios_pago" :key="mp.value" :value="mp.value">
                        {{ mp.label }}
                    </option>
                </select>

            </div>

            <BaseButton label="Editar" type="submit">
                Editar
            </BaseButton>

        </form>
    </div>

</template>

<style scoped></style>
