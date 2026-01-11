<script setup lang="ts">
import PublicFooter from '@/components/layout/PublicFooter.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-100 text-gray-900">
    <main class="flex-1 flex items-center justify-center">
      <RouterView />
    </main>

    <PublicFooter variant="auth" />
  </div>
</template>

<style scoped></style>
