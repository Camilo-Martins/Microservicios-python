<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import BaseButton from '@/components/BaseButton.vue'
import { useAddProducto } from '../composables/composables'
import useToast from '@/stores/useToast'
import { productSchema } from '../schemas/productSchema'

const props = defineProps({
    proveedores: {
        type: Array,
        required: true,
    },
})
const { trigger } = useToast()
const { sendData: sendProducto } = useAddProducto()
const emit = defineEmits(['addProduct'])

const submit = async (values, { resetForm }) => {
    console.log(values)
    try {
        await sendProducto({
            nombre_producto: values.nombre_producto,
            descripcion: values.descripcion,
            precio: values.precio,
            stock_actual: values.stock,
            categoria: values.categoria?values.categoria:'NoDefinido',
            proveedor_id: values.proveedor,
        })

        emit('addProduct')
        resetForm()
    } catch (error) {
        console.log(error)
        trigger('Ingrese nombre para agregar el producto', 'error')
    }
}
</script>

<template>
    <!-- Formulario -->
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-5 mb-8">
        <Form :validation-schema="productSchema" @submit="submit"
            class="grid grid-cols-1 md:grid-cols-7 gap-4 items-end">
            <div class="form-field">
                <div class="pb-3"><label class="form.label">Nombre Producto</label>:</div>

                <Field type="text" name="nombre_producto" class="form-input" placeholder="Ej: Arroz Grano Largo" />
            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">Descripción:</label>
                </div>

                <Field type="text" name="descripcion" class="form-input"
                    placeholder="Ej: Arroz de grano largo de calidad superior" />
            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">Precio:</label>
                </div>

                <Field type="number" name="precio" class="form-input" placeholder="Ej: $10.000" />
            </div>

            <div class="form-field">
                <div class="py-3">
                    <label class="form.label">Categoria:</label>
                </div>
                <Field as="select" class="form-input" name="categoria">
                    <option value="" disabled="">Seleccione</option>
                    <option value="">No definido</option>
                    <option value="Alimentos">Alimentos</option>
                    <option value="Bebidas">Bebidas</option>
                    <option value="Limpieza">Limpieza</option>
                    <option value="Higiene">Higiene Personal</option>
                    <option value="Tecnologia">Tecnología</option>
                    <option value="Escolares">Art. Escolares</option>
                    <option value="Regalos">Regalos</option>
                    <option value="Dulces">Dulces</option>
                </Field>
            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">Proveedor:</label>
                </div>

                <Field as="select" class="form-input" name="proveedor">
                    <option value="" disabled="">Seleccionar</option>
                    <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.id">
                        {{ proveedor.nombre_completo }} - ( {{ proveedor.nombre_empresa }} )
                    </option>
                </Field>
            </div>

            <div class="form-field">
                <div class="pb-3">
                    <label class="form.label">Stock:</label>
                </div>

                <Field type="number" name="stock" class="form-input" placeholder="Ej: 100" />
            </div>

            <BaseButton label="Agregar Personal" type="submit"> Agregar </BaseButton>
            <div class="form-field col-span-12">
                <ErrorMessage name="nombre_producto" class="text-red-600 col-span-6 italic" />
                <ErrorMessage name="precio" class="text-red-600 col-span-6 italic" />
                <ErrorMessage name="stock" class="text-red-600 col-span-6 italic" />
            </div>
        </Form>
    </div>
</template>

<style scoped></style>
