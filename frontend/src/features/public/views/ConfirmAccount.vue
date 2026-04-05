<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useConfirmAccount } from '../composables/useConfirmAccount'

const route = useRoute()
const router = useRouter()
const token = route.params.token

const { sendData, loading, error, success } = useConfirmAccount()

onMounted(async () => {
  await sendData(token)

  // redirigir después de confirmar
  setTimeout(() => {
    router.push('/login')
  }, 5000)
})
</script>

<template>
  <div class="w-full flex min-h-screen items-center justify-center px-4">
    <div class="w-full max-w-lg rounded-2xl bg-white p-8 shadow-xl space-y-6 border border-gray-200">
      <div v-if="loading">Confirmando cuenta...</div>

      <div v-else-if="error">
        <p class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-700 text-center">
          {{ error }}
        </p>
      </div>
      <div v-else-if="success">
        <h1 class="justify-center text-center font-bold uppercase text-2xl">
          Gracias por confirmar tu cuenta
        </h1>
        <h2 class="justify-center text-center">
          En unos segundos sera redirigido al inicio de sesión
        </h2>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
