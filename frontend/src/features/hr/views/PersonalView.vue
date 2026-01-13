<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate';
import { ref } from 'vue';
import { useAddPersonal } from '../composables/useAddPersonal';

import BaseButton from '@/components/BaseButton.vue';

const roles = [
    { label: 'Vendedor', value: 'vendedor' },
    { label: 'Cajero', value: 'cajero' },
    { label: 'Seguridad', value: 'seguridad' },
    { label: 'Reponedor', value: 'reponedor' },
]

const medios_pago = [
    { label: 'Transferencia', value: 'Transferencia' }, 
    { label: 'Efectivo', value: 'Efectivo' }
]

let rol = ref('');
let nombre_completo = ref('');
let telefono = ref('');
let medio_pago = ref('');
let pago_diario = ref('');
let rut = ref('');


const { sendData, loading, error } = useAddPersonal()

const submit = async () => {
    await sendData({nombre_completo:nombre_completo.value, telefono:telefono.value, rut:rut.value, rol:rol.value, pago_diario:pago_diario.value, medio_pago:medio_pago.value})
  
    //await sendData({ nombre: nombre.value, nombre_tienda: nombre_tienda.value, email: email.value, password: password.value })

 

}


</script>

<template>
    <section class="w-full px-6 py-6">
        <!-- Header -->
        <header class="mb-6">
            <h1 class="text-2xl font-semibold text-slate-800 uppercase">Personal</h1>
            <p class="text-sm text-slate-500">
                Gestión básica de empleados de la tienda
            </p>
        </header>

        <!-- Formulario -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
            <Form   @submit="submit()" class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">


                <div class="form-field">
                    <div class="pb-3">
                        <label class="form.label">Nombre</label>:
                    </div>

                    <Field type="text" name="nombre_completo" class="form-input" v-model="nombre_completo"
                        placeholder="Ej: Camilo Álvarez" />

                </div>


                <div class="form-field">
                    <div class="pb-3">
                        <label class="form.label">RUT</label>
                    </div>

                    <Field type="text" name="rut" class="form-input" v-model="rut" placeholder="Ej:12345678-9" />

                </div>

                <div class="form-field">
                    <div class="pb-3">
                        <label class="form.label">ROL</label>
                    </div>


                    <select v-model="rol" class="form-input">
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


                    <Field type="text" name="telefono" class="form-input" v-model="telefono" placeholder="912345678" />

                </div>

                <div class="form-field">

                    <div class="py-3">
                        <label class="form.label">Monto Pago</label>
                    </div>
                    <Field type="text" name="pago_diario" class="form-input" v-model="pago_diario"
                        placeholder="Ej: $20.000" />

                </div>

                <div class="form-field">
                    <div class="py-3">
                        <label class="form.label">Medio Pago</label>
                    </div>

                   <select v-model="medio_pago" class="form-input">
                        <option value="" disabled>Seleccionar</option>

                        <option v-for="mp in medios_pago" :key="mp.value" :value="mp.value">
                            {{ mp.label }}
                        </option>
                    </select>

                </div>


                <BaseButton label="Agregar Personal" type="submit">
                    Agregar
                </BaseButton>
            </Form>
        </div>

        <!-- Tabla -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
            <table class="w-full text-sm">
                <thead class="bg-slate-100 text-slate-600">
                    <tr>
                        <th class="px-4 py-3 text-left">#</th>
                        <th class="px-4 py-3 text-left">Nombre</th>
                        <th class="px-4 py-3 text-left">Rol</th>
                        <th class="px-4 py-3 text-left">Remuneración</th>
                        <th class="px-4 py-3 text-left">Estado</th>
                        <th class="px-4 py-3 text-left">Contacto</th>
                        <th class="px-4 py-3 text-right">Acción</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="border-t hover:bg-slate-50">
                        <td class="px-4 py-3">1</td>
                        <td class="px-4 py-3">1</td>
                        <td class="px-4 py-3">1</td>
                        <td class="px-4 py-3">
                            1
                        </td>
                        <td class="px-4 py-3">
                            1
                        </td>
                        <td class="px-4 py-3">1</td>
                        <td class="px-4 py-3 text-right">
                            <button class="text-blue-600 hover:underline">
                                Ver
                            </button>
                        </td>
                    </tr>


                </tbody>
            </table>
        </div>
    </section>
</template>


<style scoped></style>
