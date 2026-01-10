<script setup>
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue';

</script>

<template>
  <div class="w-full flex min-h-screen items-center justify-center px-4">
    <div
      class="
        w-full max-w-lg
        rounded-2xl
        bg-white
        p-8
        shadow-xl
        space-y-6
        border border-gray-200
      "
    >
      <!-- Título -->
      <div class="text-center space-y-1">
        <h1 class="text-2xl font-semibold text-gray-900">
          Iniciar Sesión
        </h1>
        <p class="text-sm text-gray-500">
          Ingresa para administrar tu Tienda
        </p>
      </div>

      <!-- Form -->
      <form class="space-y-4">
        <BaseInput
          label="Correo electrónico"
          type="email"
          placeholder="correo@ejemplo.com"
        />

        <BaseInput
          label="Contraseña"
          type="password"
        />

        <BaseButton
            label="Iniciar Sesión"
        >
          Iniciar Sesión
        </BaseButton>
      </form>

      <!-- Links -->
      <div class="flex justify-between text-sm text-gray-500">
        <RouterLink
          to="/register"
          class="hover:text-blue-600"
          hre
        >
          Registrate
        </RouterLink>

        <RouterLink
          to="/reset-password"
          class="hover:text-blue-600"
        >
          Recuperar clave
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
