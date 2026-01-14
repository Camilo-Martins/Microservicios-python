import { ref, readonly } from 'vue'
import {  getPersonaService } from '../services/getPersonaService'


export function useGetPersona() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)
  const success = ref(false)

  const sendData = async (id) => {
    loading.value = true
    error.value = null
      success.value = false

    try {
        data.value = await getPersonaService(id)
        success.value = true
        console.log(data.value)
      
    } catch (e) {
          if (e?.data?.message) {
              window.location.href = `/panel/personal`;
        error.value = e.data.message
        
      } else{
          window.location.href = `/panel/personal`;
         error.value = 'Hubo un problema al encontrar perfil'
         
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