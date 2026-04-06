<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import BaseButton from '@/components/BaseButton.vue'
import { useRegister } from '../composables/useRegister'

let nombre = ref('')
let nombre_tienda = ref('')
let email = ref('')
let password = ref('')
let succes = false
const router = useRouter()

const { sendData, loading, error } = useRegister()

const submit = async () => {
  await sendData({
    nombre: nombre.value,
    username: nombre.value,
    nombre_tienda: nombre_tienda.value,
    email: email.value,
    password: password.value,
  })

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
        <h1 class="text-2xl font-semibold text-gray-900">Crear cuenta</h1>
        <p class="text-sm text-gray-500">Registra tu tienda para comenzar</p>
      </div>

      <!-- Form -->
      <Form @submit="submit()" class="space-y-4">
        <p v-if="error" class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-700">
          {{ error }}
        </p>
        <p v-if="succes"
          class="rounded-md bg-green-50 border border-green-200 px-3 py-2 text-sm text-green-800 text-center font-bold uppercase">
          Cuenta registrada exitosamente
        </p>

        <div class="form-field">
          <label class="form.label">Nombre completo</label>
          <Field type="text" name="nombre" class="form-input" v-model="nombre" placeholder="Ej: Camilo Álvarez" />
          <ErrorMessage name="nombre" class="text-red-700 font-bold uppercase" />
        </div>

        <div class="form-field">
          <label class="form.label">Nombre Tienda</label>
          <Field type="text" name="nombre_tienda" class="form-input" v-model="nombre_tienda"
            placeholder="Ej: Pepito Store" />
          <ErrorMessage name="nombre_tienda" class="text-red-700 font-bold uppercase" />
        </div>

        <div class="form-field">
          <label class="form.label">Email</label>
          <Field type="text" name="email" class="form-input" v-model="email" placeholder="Ej: Camilo Álvarez" />
          <ErrorMessage name="email" class="text-red-700 font-bold uppercase" />
        </div>

        <div class="form-field">
          <label class="form.label">Contraseña</label>
          <Field type="password" name="password" class="form-input" v-model="password"
            placeholder="Ej: ***********" />
          <ErrorMessage name="password" class="text-red-700 font-bold uppercase" />
        </div>

        <BaseButton label="Registrarse" type="submit"> Register </BaseButton>
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
