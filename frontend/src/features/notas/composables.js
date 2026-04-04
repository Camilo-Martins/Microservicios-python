// composables/useRegister.ts
import { ref, readonly } from 'vue'
import { getNota, addNota } from './services'

export function useGetNota() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await getNota(body)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se obtenieron las notas'
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

export function useAddNota() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await addNota(body)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
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
