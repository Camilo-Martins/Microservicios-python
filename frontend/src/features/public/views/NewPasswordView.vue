<script setup>
import { Form, Field, ErrorMessage } from 'vee-validate';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useNewPassword } from '../composables/useNewPassword';
import BaseButton from '@/components/BaseButton.vue';

let password = ref('')
const route = useRoute();
const router = useRouter();
const token = route.params.token;


const { sendData, loading, error, success } = useNewPassword()

const submit = async () => {
  console.log(password.value)
  await sendData(token, { password: password.value })


  if (loading.value == false) {
    setTimeout(() => {
      router.push('/login')
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
          Recupera tu contraseña
        </h1>
        <p class="text-sm text-gray-500">
          Y recupera tu información
        </p>
      </div>

      <!-- Form -->
      <Form @submit="submit()" class="space-y-4">
        <p v-if="error" class="rounded-md bg-red-50 border border-red-200 px-3 py-2 text-sm text-red-700">
          {{ error }}
        </p>

        <div class="form-field">
          <ErrorMessage name="email" class="error-text" />
          <label class="form.label">Password</label>
          <Field type="password" name="password" class="form-input" v-model="password" placeholder="Ej: *******" />
        </div>


        <BaseButton label="CambiarPass" type="submit">
          Cambiar clave
        </BaseButton>
      </Form>

      <!-- Links -->
      <div class="flex justify-between text-sm text-gray-500">
        <RouterLink to="/login" class="hover:text-blue-600" hre>
          Iniciar sesión
        </RouterLink>

        <RouterLink to="/reset-password" class="hover:text-blue-600">
          Recuperar clave
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
