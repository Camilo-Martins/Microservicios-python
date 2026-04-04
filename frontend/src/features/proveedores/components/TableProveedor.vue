<script setup>
import {computed } from 'vue'
import useToast from '@/stores/useToast'

const props = defineProps({
  proveedoreslist: {
    type: Array,
    required: true,
  }
 
})

</script>

<template>
 <div class="max-h-96 overflow-y-auto rounded-xl shadow-sm border border-slate-200">

    <table
      class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200"
    >
      <thead class="bg-slate-100 text-slate-600">
        <tr>
          <th class="px-4 py-3 text-left w-32">Nombre</th>
          <th class="px-4 py-3 text-center">Rut</th>
          <th class="px-4 py-3 text-center w-60">Telefono</th>
          <th class="px-4 py-3 text-center">Nombre Empresa</th>
          <th class="px-4 py-3 text-center">Email</th>
          <th class="px-4 py-3 text-center">Observaciones</th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="proveedor in proveedoreslist"
          :key="proveedor.id"
          class="border-t hover:bg-slate-50 transition"
        >
          <!-- Día -->
          <td class="px-4 py-3 font-medium text-slate-700 align-top">
            {{ proveedor.nombre_completo }}
          </td>

          <!-- Selector compacto -->
          <td class="px-4 py-3 align-top">
            {{ proveedor.rut }}
          </td>

          
        </tr>
      </tbody>
    </table>
  </div>
</template>
<style scoped></style>
