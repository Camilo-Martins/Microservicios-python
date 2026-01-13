import { ref, readonly } from 'vue'
import { deletePersonalService } from '../services/deletePersonalService'


export function useDeletePersonal() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)
  const success = ref(false)

  const sendData = async (id) => {
    loading.value = true
    error.value = null
      success.value = false

    try {
      data.value = await deletePersonalService(id)
       success.value = true
    } catch (e) {
          if (e?.data?.message) {
        error.value = e.data.message
      } else{
         error.value = 'Hubo un problema al confirmar la cuenta'
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
      success: readonly(success),
  }
}