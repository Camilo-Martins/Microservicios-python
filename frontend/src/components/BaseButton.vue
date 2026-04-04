<script setup lang="ts">
defineProps<{
  type?: string
}>()
</script>

<template>
  <button
    :type="type || 'submit'"
    class="w-full rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 transition-colors"
  >
    <slot />
  </button>
</template>
<style scoped></style>
