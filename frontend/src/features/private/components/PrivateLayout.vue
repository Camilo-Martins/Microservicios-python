<script setup>
import PublicFooter from '@/components/layout/PublicFooter.vue'
import PrivateNav from './PrivateNav.vue'
</script>

<template>
  <div class="min-h-screen flex flex-col bg-gray-50">
    <PrivateNav />

    <main class="flex-1 px-6 py-8">
      <router-view />
    </main>

    <PublicFooter />
  </div>
</template>
<style scoped></style>
