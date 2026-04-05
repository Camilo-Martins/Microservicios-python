<script setup>
import { Form, Field } from 'vee-validate'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import useToast from '@/stores/useToast'
import BaseButton from '@/components/BaseButton.vue'
import { useLogin } from '../composables/useLogin'

const router = useRouter()
const { sendData } = useLogin()

const { trigger } = useToast()
let password = ref('')
let email = ref('')

const submit = async () => {
  try {
    await sendData({ email: email.value, password: password.value })
    router.push('/panel')
  } catch (error) {
    trigger('Ingrese credenciales válidas')
  }
}
</script>

<template>
  <div class="w-full flex min-h-screen items-center justify-center px-4">
    <div class="w-full max-w-lg rounded-2xl bg-white p-8 shadow-xl space-y-6 border border-gray-200">
      <!-- Título -->
      <div class="text-center space-y-1">
        <h1 class="text-2xl font-semibold text-gray-900">Iniciar Sesión</h1>
        <p class="text-sm text-gray-500">Ingresa para administrar tu Tienda</p>
      </div>

      <!-- Form -->
      <Form @submit="submit()" class="space-y-4">
        <div class="form-field">
          <label class="form.label">Email</label>
          <Field type="text" name="email" class="form-input" v-model="email" placeholder="Ej: Camilo Álvarez" />
        </div>

        <div class="form-field">
          <label class="form.label">Contraseña</label>
          <Field type="password" name="password" class="form-input" v-model="password" placeholder="***********" />
        </div>

        <BaseButton label="Registrarse" type="submit"> Ingesar </BaseButton>
      </Form>

      <!-- Links -->
      <div class="flex justify-between text-sm text-gray-500">
        <RouterLink to="/register" class="hover:text-blue-600" hre> Registrate </RouterLink>

        <RouterLink to="/reset-password" class="hover:text-blue-600"> Recuperar clave </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
