<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import BaseButton from '@/components/BaseButton.vue';
import { useLogin } from '../composables/useLogin';
import { useAuthStore } from '@/stores/authStore';

const router = useRouter();
const { sendData, loading, error } = useLogin()

let store = useAuthStore();
let password = ref('');
let email = ref('');

const submit = async () => {
  console.log({email: email.value, password: password.value })
  await sendData({email: email.value, password: password.value })

  if (loading.value == false) {
    setTimeout(() => {
      router.push('/panel')
    }, 1000)
  }

}


</script>

<template>
  <div class="w-full flex min-h-screen items-center justify-center px-4">
    <div class="
        w-full max-w-lg
        rounded-2xl
        bg-white
        p-8
        shadow-xl
        space-y-6
        border border-gray-200
      ">
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
      <Form  @submit="submit()" class="space-y-4">
        <p v-if="error" class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-700">
          {{ error }}
        </p>

        <div class="form-field">
          <ErrorMessage name="email" class="error-text" />
          <label class="form.label">Email</label>
          <Field type="text" name="email" class="form-input" v-model="email" placeholder="Ej: Camilo Álvarez" />
        </div>

        <div class="form-field">
          <ErrorMessage name="password" class="error-text" />
          <label class="form.label">Contraseña</label>
          <Field type="password" name="password" class="form-input" v-model="password"
            placeholder="Ej: Camilo Álvarez" />
        </div>


        <BaseButton label="Registrarse" type="submit">
          Register
        </BaseButton>
      </Form>

      <!-- Links -->
      <div class="flex justify-between text-sm text-gray-500">
        <RouterLink to="/register" class="hover:text-blue-600" hre>
          Registrate
        </RouterLink>

        <RouterLink to="/reset-password" class="hover:text-blue-600">
          Recuperar clave
        </RouterLink>
      </div>
      
    </div>
  </div>
</template>

<style scoped></style>
