<script setup>

import { useGetProveedorLista } from '../proveedores/composables/composables';
import AddProduct from './components/AddProduct.vue';
import TableProduct from './components/TableProduct.vue';
import { useGetProductos} from './composables/composables';
import { onMounted, ref } from 'vue';

const { sendData, data } = useGetProductos()
const { sendData: sendProveedor, data: dataProveedor } = useGetProveedorLista()
let productoslist = ref([])
const proveedores = ref([])
const filtros = ref({
    proveedor: '',
    categoria: '',
})



const fetchProveedores = async () => {
    await sendProveedor()
    proveedores.value = dataProveedor.value.data
}

const fetchProductos = async () => {
 try {

   const params = {}

        if (filtros.value.proveedor) {
            params.proveedor = filtros.value.proveedor
        }

        if (filtros.value.categoria) {
            params.categoria = filtros.value.categoria
        }

    await sendData(params)
    productoslist.value = data.value.data
 } catch (error) {
    console.log(error)
 }
}
const handleFiltersChange = async (filters) => {
    filtros.value = filters
    await fetchProductos()
}


onMounted(() => {
    fetchProductos()
    fetchProveedores()
})



</script>

<template>
  <section class="w-full px-6 py-6">
    <!-- Header -->
    <header class="mb-6">
      <h1 class="text-2xl font-semibold text-slate-800 uppercase">Productos</h1>
      <p class="text-sm text-slate-500">Gestión de Productos</p>
    </header>

    
      <div>
        <AddProduct :proveedores="proveedores"  @addProduct="fetchProductos" />
      </div>
      <div>
        <TableProduct :productoslist="productoslist" :proveedores="proveedores"   @filters-change="handleFiltersChange" @updatedProducto="fetchProductos" />
      </div>
      
    
  </section>
</template>
<style scoped></style>
