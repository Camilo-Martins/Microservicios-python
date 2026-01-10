// composables/useRegister.ts
import { ref, readonly } from 'vue'
import { register } from '../services/registerService'

export function useRegister() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await register(body)
    } catch (e) {
          if (e?.data?.message) {
        error.value = e.data.message
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
