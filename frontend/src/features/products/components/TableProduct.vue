<script setup>
import { useGetProveedorLista } from '@/features/proveedores/composables/composables'
import { Form, Field, ErrorMessage } from 'vee-validate'
import { onMounted, ref, watch } from 'vue'

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
const emit = defineEmits(['filters-change'])

const categoriaSeleccionada = ref('')
const proveedorSeleccionado = ref('')

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
            <label class="block text-xs text-slate-500 mb-1">
                Categoría
            </label>

            <select
                v-model="categoriaSeleccionada"
                class="w-full max-w-xs rounded-md border border-slate-300 px-3 py-1.5 text-sm focus:ring-1 focus:ring-slate-400"
            >
                <option value="">Todas</option>
                <option value="Alimentos">Alimentos</option>
                <option value="Bebidas">Bebidas</option>
                <option value="Limpieza">Limpieza</option>
                <option value="Higiene Personal">Higiene Personal</option>
            </select>
        </div>

        <!-- Proveedor -->
        <div>
            <label class="block text-xs text-slate-500 mb-1">
                Proveedor
            </label>

            <select
                v-model="proveedorSeleccionado"
                class="w-full max-w-xs rounded-md border border-slate-300 px-3 py-1.5 text-sm focus:ring-1 focus:ring-slate-400"
            >
                <option value="">Todos</option>
                <option
                    v-for="proveedor in proveedores"
                    :key="proveedor.id"
                    :value="proveedor.nombre_completo"
                >
                    {{ proveedor.nombre_completo }}
                </option>
            </select>
        </div>
    </div>
</div>

    <br />

    <div class="max-h-96 overflow-y-auto rounded-xl shadow-sm border border-slate-200">
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
                        <span>
                            {{ productos.nombre_producto ? productos.nombre_producto : 'No definido' }}
                        </span>
                    </td>

                    <!-- Descripcion -->
                    <td class="px-4 py-3 text-left truncate max-w-xs" colspan="1">
                        <span>{{ productos.descripcion ? productos.descripcion : 'No definido' }}</span>
                    </td>

                    <!-- Precio -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <span>${{ productos.precio ? productos.precio : '0.00' }}</span>
                    </td>

                    <!-- Categoría -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <span>{{ productos.categoria ? productos.categoria : 'No definido' }}</span>
                    </td>

                    <!-- Proveedor -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="1">
                        <span>{{ productos.proveedor ? productos.proveedor : 'No definido' }}</span>
                    </td>

                    <!-- Stock -->
                    <td class="px-4 py-3 text-center truncate max-w-xs" colspan="6">
                        <span>{{ productos.stock ? productos.stock : '0' }}</span>
                    </td>

                    <!-- Productos -->
                </tr>
            </tbody>
        </table>
    </div>
</template>
<style scoped></style>
