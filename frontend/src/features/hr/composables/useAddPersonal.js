// composables/useRegister.ts
import { ref, readonly } from 'vue'
import { addPersonal } from '../services/addPersonal'

export function useAddPersonal() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await addPersonal(body)
    } catch (e) {
          if (e?.data?.message) {
        error.value = e.data.message
      } else{
         error.value = 'No se pudo completar el registro'
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
