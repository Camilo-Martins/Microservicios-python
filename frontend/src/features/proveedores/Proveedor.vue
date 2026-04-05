<script setup>
import { ref, onMounted } from 'vue'
import AddProveedor from './components/AddProveedor.vue'
import TableProveedor from './components/TableProveedor.vue'
import { useGetProveedor } from './composables/composables'

const { sendData, data } = useGetProveedor()

let proveedoreslist = ref([])

const fetchProveedores = async () => {
  await sendData()

  proveedoreslist.value = data.value.data
}

onMounted(() => {
  fetchProveedores()
})
</script>

<template>
  <section class="w-full px-6 py-6">
    <!-- Header -->
    <header class="mb-6">
      <h1 class="text-2xl font-semibold text-slate-800 uppercase">Proveedores</h1>
      <p class="text-sm text-slate-500">Gestión de Proveedores</p>
    </header>

    <div class="grid grid-cols-12 gap-6">
      <div class="col-span-3">
        <AddProveedor @created="fetchProveedores" />
      </div>

      <div class="col-span-9">
        <TableProveedor :proveedoreslist="proveedoreslist" @updatedProveedor="fetchProveedores" />
      </div>
    </div>
  </section>
</template>
<style scoped></style>
