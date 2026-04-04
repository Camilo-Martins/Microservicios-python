<script setup lang="ts">
defineProps<{
  label: string
  type?: string
  placeholder?: string
}>()
</script>

<template>
  <div class="space-y-1">
    <label class="block text-sm font-medium text-gray-700">
      {{ label }}
    </label>

    <input
      :type="type || 'text'"
      :placeholder="placeholder"
      class="w-full rounded-lg bg-gray-50 border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    />
  </div>
</template>
