// composables/useRegister.ts
import { ref, readonly } from 'vue'
import { login } from '../services/loginService'
import { useAuthStore } from '@/stores/authStore'

export function useLogin() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (body) => {
    loading.value = true
    error.value = null
    let store = useAuthStore();

    try {
      data.value = await login(body)
     
      store.iniciarSesion(data.value.token)
    } catch (e) {
      console.log(e)
          if (e?.data?.message) {
            
        error.value = e.data.message
      } else{
         error.value = 'No se pudo iniciar sesión'
      }
      throw e
    } finally {
      loading.value = false
      
    }
  }

  return {
    sendData,
    data: readonly(data),
    loading: readonly(loading),
    error: readonly(error),
  }
}
