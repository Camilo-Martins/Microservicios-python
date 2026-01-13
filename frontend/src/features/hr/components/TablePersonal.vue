<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  },
  selectedId: {
    type: Number,
    default: null
  }
})

const emit = defineEmits(['toggle-status', 'select'])
</script>

<template>
<div class="max-h-96 overflow-y-auto bg-white rounded-xl shadow-sm border border-slate-200">
  <table class="min-w-full border-collapse text-center">
        <thead class="bg-slate-100 text-slate-600">
            <tr>
             
                <th class="px-4 py-3 ">Nombre</th>
                <th class="px-4 py-3 ">Rut</th>
                <th class="px-4 py-3 ">Rol</th>
                <th class="px-4 py-3 ">Remuneración ($)</th>
                <th class="px-4 py-3 ">Estado</th>
                <th class="px-4 py-3 ">Contacto</th>
                <th class="px-4 py-3 ">Acción</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="persona in items" :key="persona.id" class="border-t hover:bg-slate-200">
                <td class="px-4 py-3"> {{ persona.nombre_completo }}</td>
                <td class="px-4 py-3">{{ persona.rut }}</td>
                <td class="px-4 py-3">{{ persona.rol }}</td>
                <td class="px-4 py-3">{{ persona.pago_diario }}</td>
                <td class="px-4 py-3">
                  <button
                        @click="emit('toggle-status', persona.id)"
                        :class="persona.is_active
                            ? 'px-3 py-1 text-sm rounded bg-green-100 text-green-700 hover:bg-green-200'
                            : 'px-3 py-1 text-sm rounded bg-red-100 text-red-700 hover:bg-red-200'"
                        >
                        {{ persona.is_active ? 'Activo' : 'Inactivo' }}
                        </button>

                </td>

                <td class="px-4 py-3">
                    <a :href="`https://wa.me/${(persona.telefono).trim()}`" target="_blank" rel="noopener noreferrer"
                        class="text-green-600 hover:underline font-medium">
                        ENVIAR WSP
                    </a>
                </td>
                <td class="px-4 py-3">

                    <a :href="`/panel/persona/${persona.id}`" class="text-blue-600 hover:underline font-medium">
                        VER
                    </a>
                </td>
            </tr>

        </tbody>

    </table>
</div>
</template>


<style scoped></style>
