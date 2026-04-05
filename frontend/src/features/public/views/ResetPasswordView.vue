<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import BaseButton from '@/components/BaseButton.vue'
import { useResetPassword } from '../composables/useResetPassword'
import { resetSchema } from '../schemas/validacionesSchemas'

let email = ref('')
let succes = false
const router = useRouter()

const { sendData, loading, error } = useResetPassword()

const submit = async () => {
  await sendData({ email: email.value })

  if (loading.value == false) {
    succes = true
    setTimeout(() => {
      router.push('/login')
    }, 3000)
  }
}
</script>

<template>
  <div class="w-full flex min-h-screen items-center justify-center px-4">
    <div class="w-full max-w-lg rounded-2xl bg-white p-8 shadow-xl space-y-6 border border-gray-200">
      <!-- Título -->
      <div class="text-center space-y-1">
        <h1 class="text-2xl font-semibold text-gray-900">Recupera tu contraseña</h1>
        <p class="text-sm text-gray-500">Completando con tu correo el siguiente campo</p>
      </div>

      <!-- Form -->
      <Form :validation-schema="resetSchema" @submit="submit()" class="space-y-4">
        <p v-if="error"
          class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-800 text-center font-bold uppercase">
          {{ error }}
        </p>

        <p v-if="succes"
          class="rounded-md bg-green-50 border border-green-200 px-3 py-2 text-sm text-green-800 text-center font-bold uppercase">
          Revisa tu bandeja de entrada
        </p>

        <div class="form-field">
          <label class="form.label">Email</label>
          <Field type="text" name="email" class="form-input" v-model="email" placeholder="Guaripolo@gmail.com" />
          <ErrorMessage name="email" class="text-red-600  capitalize" />
        </div>

        <BaseButton label="Registrarse" type="submit"> Enviar </BaseButton>
      </Form>

      <!-- Links -->
      <div class="flex justify-between text-sm text-gray-500">
        <RouterLink to="/login" class="hover:text-blue-600" hre> Iniciar sesión </RouterLink>

        <RouterLink to="/reset-password" class="hover:text-blue-600"> Recuperar clave </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
