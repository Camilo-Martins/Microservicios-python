<script setup>
defineProps({
  items: {
    type: Array,
    required: true,
  },
  selectedId: {
    type: Number,
    default: null,
  },
})

const emit = defineEmits(['toggle-status', 'select', 'persona-data'])
</script>

<template>
  <div class="max-h-96 overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
    <div>
      <h5 class="text-center py-4 font-bold">Personal</h5>
    </div>
    <table
      class="min-w-full border-collapse text-sm overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200"
    >
      <thead class="bg-slate-100 text-slate-600">
        <tr>
          <th class="px-4 py-3 text-left">Nombre</th>
          <th class="px-4 py-3 text-center">Rut</th>
          <th class="px-4 py-3 text-center">Pago</th>
          <th class="px-4 py-3 text-center">Estado</th>
          <th class="px-4 py-3 text-center">Contacto</th>
          <th class="px-4 py-3 text-center">Acción</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="persona in items" :key="persona.id" class="border-t hover:bg-slate-200">
          <td class="px-4 py-3 text-left">{{ persona.nombre_completo }}</td>
          <td class="px-4 py-3 text-center">{{ persona.rut }}</td>
          <td class="px-4 py-3 text-center">${{ persona.pago_diario? persona.pago_diario : 0 }}</td>
          <td class="px-4 py-3 text-center">
            <button
              @click="emit('toggle-status', persona.id)"
              :class="
                persona.is_active
                  ? 'px-3 py-1 text-sm rounded bg-green-100 text-green-700 hover:bg-green-200'
                  : 'px-3 py-1 text-sm rounded bg-red-100 text-red-700 hover:bg-red-200'
              "
            >
              {{ persona.is_active ? 'Activo' : 'Inactivo' }}
            </button>
          </td>

          <td class="px-4 py-3 text-center">
            <a
              :href="`https://wa.me/${persona.telefono.trim()}`"
              target="_blank"
              rel="noopener noreferrer"
              class="text-green-600 hover:underline font-medium"
            >
              ENVIAR WSP
            </a>
          </td>
          <td class="px-4 py-3 text-center">
            <a
              @click="emit('personta-data', persona.id)"
              :href="`/panel/persona/${persona.id}`"
              class="text-blue-600 hover:underline font-medium"
            >
              Editar
            </a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
