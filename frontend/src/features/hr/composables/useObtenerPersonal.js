// composables/useRegister.ts
import { ref, readonly } from 'vue'
import { obtenerPersonal } from '../services/obtenerPersonal'

export function useObtenerPersonal() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async () => {
    loading.value = true
    error.value = null

    try {
      data.value = await obtenerPersonal()
    } catch (e) {
          if (e?.data?.message) {
        error.value = e.data.message
      } else{
         error.value = 'No se pudo obtener la data'
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
