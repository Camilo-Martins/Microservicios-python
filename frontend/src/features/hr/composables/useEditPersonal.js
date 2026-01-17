// composables/useRegister.ts
import { ref, readonly } from 'vue'
import { editPersonalServive } from '../services/editPersonalService'

export function useEditPersonal() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (id, body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await editPersonalServive(id, body)
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
