<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate';
import { reactive } from 'vue';
import { ref } from 'vue';

import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue';
import { useRegister } from '../composables/useRegister';
import { registroSchema } from '../schemas/validacionesSchemas';


let nombre = ref('');
let email = ref('');
let password = ref('')

const { sendData, loading, error } = useRegister()

const submit = async () => {
  await sendData({nombre:nombre.value, email:email.value, password:password.value})

}

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
          Crear cuenta
        </h1>
        <p class="text-sm text-gray-500">
          Registra tu tienda para comenzar
        </p>
      </div>

      <!-- Form -->
      <Form :validation-schema="registroSchema" @submit="submit()" class="space-y-4">
  <p
  v-if="error"
  class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-700"
>
  {{ error }}
</p>

           <div class="form-field">
            <ErrorMessage name="nombre" class="error-text" />
            <label class="form.label">Nombre completo</label>
            <Field
              type="text"
              name="nombre"
              class="form-input"
              v-model="nombre"
              placeholder="Ej: Camilo Álvarez"
            />
          </div>

        

            <div class="form-field">
            <ErrorMessage name="email" class="error-text" />
            <label class="form.label">Email</label>
            <Field
              type="text"
              name="email"
              class="form-input"
              v-model="email"
              placeholder="Ej: Camilo Álvarez"
            />
          </div>

                <div class="form-field">
            <ErrorMessage name="password" class="error-text" />
            <label class="form.label">Contraseña</label>
            <Field
              type="password"
              name="password"
              class="form-input"
              v-model="password"
              placeholder="Ej: Camilo Álvarez"
            />
          </div>


        <BaseButton
            label="Registrarse"
            type="submit"
        >
          Register
        </BaseButton>
      </Form>

      <!-- Links -->
      <div class="flex justify-between text-sm text-gray-500">
        <RouterLink
          to="/login"
          class="hover:text-blue-600"
          hre
        >
          Iniciar sesión
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
