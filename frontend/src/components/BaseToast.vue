<script setup>
useToast
import useToast from '@/stores/useToast'
import { computed } from 'vue'

const { show, message, type } = useToast()

const toastClass = computed(() => {
  return {
    error: 'bg-red-700 text-white font-bold uppercase',
    success: 'bg-green-700 text-white font-bold uppercase',
    info: 'bg-slate-700 text-white font-bold uppercase',
  }[type.value]
})
</script>

<template>
  <transition name="fade">
    <div
      v-if="show"
      class="fixed top-5 right-5 z-50 max-w-sm w-full px-4 py-3 rounded-lg shadow-lg text-sm font-medium text-center"
      :class="toastClass"
    >
      {{ message }}
    </div>
  </transition>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
