import { ref, readonly } from 'vue'
import { resetPassword } from '../services/resetPasswordService'

export function useResetPassword() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)
  const success = ref(false)

  const sendData = async (token) => {
    loading.value = true
    error.value = null
      success.value = false

    try {
      data.value = await resetPassword(token)
       success.value = true
    } catch (e) {
          if (e?.data?.message) {
        error.value = e.data.message
      } else{
         error.value = 'Hubo un problema al enviar correo'
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
