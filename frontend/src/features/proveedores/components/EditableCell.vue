<template>
  <td class="px-4 py-3 text-left truncate max-w-xs" :colspan="colspan">
    <input
      v-if="isEditing"
      :value="modelValue"
      type="text"
      class="w-full rounded border border-slate-300 px-2 py-1"
      @input="$emit('update:modelValue', $event.target.value)"
      @blur="$emit('save')"
      @keyup.enter="$emit('save')"
      @keyup.esc="$emit('cancel')"
    />

    <span
      v-else
      class="block w-full cursor-pointer"
      @click="$emit('edit')"
    >
      {{ displayValue? displayValue: 'No Definido' }}
    </span>
  </td>
</template>

<script setup>
defineProps({
  modelValue: {
    type: String,
    default: '',
  },
  displayValue: {
    type: String,
    default: '',
  },
  isEditing: {
    type: Boolean,
    default: false,
  },
  colspan: {
    type: [Number, String],
    default: 1,
  },
})

defineEmits(['update:modelValue', 'edit', 'save', 'cancel'])
</script>