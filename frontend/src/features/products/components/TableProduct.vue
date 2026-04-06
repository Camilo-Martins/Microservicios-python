<script setup>
import { ref, watch } from 'vue'
import useToast from '@/stores/useToast'
import { useEditProducto } from '../composables/composables'

const props = defineProps({
    productoslist: {
        type: Array,
        required: true,
    },
    proveedores: {
        type: Array,
        required: true,
    },
})

const categorias = ['Alimentos', 'Bebidas', 'Limpieza', 'Higiene']
const { trigger } = useToast()
const emit = defineEmits(['filters-change', 'updatedProducto'])
const { sendData } = useEditProducto()
const editing = ref({
    id: null,
    field: null,
    value: '',
})
const categoriaSeleccionada = ref('')
const proveedorSeleccionado = ref('')

const startEdit = (proveedor, field) => {
    editing.value.id = proveedor.id
    editing.value.field = field
    editing.value.value = proveedor[field] ?? ''
}

const cancelEdit = () => {
    editing.value.id = null
    editing.value.field = null
    editing.value.value = ''
}

const saveEdit = async (producto) => {
    const { field, value } = editing.value

    if (!field) return

    if (value === producto[field]) {
        cancelEdit()
        return
    }

    const confirmed = window.confirm('¿Guardar cambios?')
    if (!confirmed) {
        cancelEdit()
        return
    }

    try {
        await sendData(producto.id, {
            [field]: value,
        })

        emit('updatedProducto')
        producto[field] = value
    } catch (error) {
        trigger('Error al actualizar el producto', 'error')
    } finally {
        cancelEdit()
    }
}

watch([categoriaSeleccionada, proveedorSeleccionado], () => {
    emit('filters-change', {
        categoria: categoriaSeleccionada.value,
        proveedor: proveedorSeleccionado.value,
    })
})
</script>

<template>
    <div class="bg-white border border-slate-200 rounded-xl p-4 shadow-sm max-w-3xl">
        <h3 class="text-sm font-semibold text-slate-600 mb-3">Filtros</h3>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-3xl">
            <!-- Categoría -->
            <div>
                <label class="block text-xs text-slate-500 mb-1"> Categoría </label>

                <select v-model="categoriaSeleccionada"
                    class="w-full max-w-xs rounded-md border border-slate-300 px-3 py-1.5 text-sm focus:ring-1 focus:ring-slate-400">
                    <option value="">Todas</option>
                    <option value="NoDefinido">No definido</option>
                    <option value="Alimentos">Alimentos</option>
                    <option value="Bebidas">Bebidas</option>
                    <option value="Limpieza">Limpieza</option>
                    <option value="Higiene">Higiene Personal</option>
                     <option value="Tecnologia">Tecnología</option>
                    <option value="Escolares">Art. Escolares</option>
                    <option value="Regalos">Regalos</option>
                    <option value="Dulces">Dulces</option>
                </select>
            </div>

            <!-- Proveedor -->
            <div>
                <label class="block text-xs text-slate-500 mb-1"> Proveedor </label>

                <select v-model="proveedorSeleccionado"
                    class="w-full max-w-xs rounded-md border border-slate-300 px-3 py-1.5 text-sm focus:ring-1 focus:ring-slate-400">
                    <option value="">Todos</option>
                    <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.nombre_completo">
                        {{ proveedor.nombre_completo }}
                    </option>
                </select>
            </div>
        </div>
    </div>

    <br />

    <div class="max-h-54 overflow-y-auto rounded-xl shadow-sm border border-slate-200">
        <table
            class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
            <thead class="bg-slate-100 text-slate-600">
                <tr>
                    <th class="px-4 py-3 text-left" colspan="1">Nombre Producto</th>
                    <th class="px-4 py-3 text-left" colspan="1">Descripcion</th>
                    <th class="px-4 py-3 text-center" colspan="1">Precio</th>
                    <th class="px-4 py-3 text-center" colspan="1">Categoría</th>
                    <th class="px-4 py-3 text-center" colspan="1">Proveedor</th>
                    <th class="px-4 py-3 text-center" colspan="1">Stock</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="productos in productoslist" :key="productos.id"
                    class="border-t hover:bg-slate-50 transition cursor-pointer hover:bg-slate-200"
                    title="Haz doble clic para editar">
                    <!-- Nombre -->
                    <td class="px-4 py-3 text-left truncate max-w-xs" colspan="1">
                        <input v-if="editing.id === productos.id && editing.field === 'nombre_producto'"
                            v-model="editing.value" type="text" class="w-full rounded border border-slate-300 px-2 py-1"
                            @blur="saveEdit(productos)" @keyup.enter="saveEdit(productos)" @keyup.esc="cancelEdit" />
                        <span v-else class="block w-full cursor-pointer"
                            @click="startEdit(productos, 'nombre_producto')">
                            {{ productos.nombre_producto ? productos.nombre_producto : 'No definido' }}
                        </span>
                    </td>

                    <!-- Descripcion -->
                    <td class="px-4 py-3 text-left truncate max-w-xs" colspan="1">
                        <input v-if="editing.id === productos.id && editing.field === 'descripcion'"
                            v-model="editing.value" type="text" class="w-full rounded border border-slate-300 px-2 py-1"
                            @blur="saveEdit(productos)" @keyup.enter="saveEdit(productos)" @keyup.esc="cancelEdit" />
                        <span v-else class="block w-full cursor-pointer" @click="startEdit(productos, 'descripcion')">
                            {{ productos.descripcion ? productos.descripcion : 'No definido' }}
                        </span>
                    </td>

                    <!-- Precio -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <input v-if="editing.id === productos.id && editing.field === 'precio'" v-model="editing.value"
                            type="text" class="w-full rounded border border-slate-300 px-2 py-1"
                            @blur="saveEdit(productos)" @keyup.enter="saveEdit(productos)" @keyup.esc="cancelEdit" />
                        <span v-else class="block w-full cursor-pointer" @click="startEdit(productos, 'precio')">
                            ${{ productos.precio ? productos.precio : '0.00' }}
                        </span>
                    </td>

                    <!-- Categoria-->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <select v-if="editing.id === productos.id && editing.field === 'categoria'"
                            v-model="editing.value" class="w-full rounded border border-slate-300 px-2 py-1"
                            @change="saveEdit(productos)" @keyup.esc="cancelEdit">
                            <option value="" disabled>Seleccione</option>
                            <option v-for="categoria in categorias" :key="categoria" :value="categoria">
                                {{ categoria }}
                            </option>
                        </select>

                        <span v-else class="block w-full cursor-pointer" @click="startEdit(productos, 'categoria')">
                            {{ productos.categoria == 'NoDefinido' ? 'No definido' : productos.categoria }}
                        </span>
                    </td>

                    <!-- Proveedor -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <select v-if="editing.id === productos.id && editing.field === 'proveedor_id'"
                            v-model="editing.value" class="w-full rounded border border-slate-300 px-2 py-1"
                            @change="saveEdit(productos)" @keyup.esc="cancelEdit">
                            <option value="" disabled>Seleccione proveedor</option>
                            <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.id">
                                {{ proveedor.nombre_completo }}
                            </option>
                        </select>
                        <span v-else class="block w-full cursor-pointer" @click="startEdit(productos, 'proveedor_id')">
                            {{ productos.proveedor || 'No definido' }}
                        </span>
                    </td>

                    <!-- Proveedor -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <input v-if="editing.id === productos.id && editing.field === 'stock_actual'"
                            v-model="editing.value" type="number"
                            class="w-full rounded border border-slate-300 px-2 py-1" @blur="saveEdit(productos)"
                            @keyup.enter="saveEdit(productos)" @keyup.esc="cancelEdit" />
                        <span v-else class="block w-full cursor-pointer" @click="startEdit(productos, 'stock_actual')">
                            {{ productos.stock_actual ? productos.stock_actual : '0' }}
                        </span>
                    </td>

                    <!-- Productos -->
                </tr>
            </tbody>
        </table>
    </div>
</template>
<style scoped></style>
