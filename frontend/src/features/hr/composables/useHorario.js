// composables/useRegister.ts
import { ref, readonly } from 'vue'
import {
  addHorarioService,
  asignarPersonalService,
  desasignarPersonalService,
  getHorarioService,
} from '../services/horarioService'

export function useAddHorario() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async () => {
    loading.value = true
    error.value = null

    try {
      data.value = await addHorarioService()
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se pudo crear el horario'
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

export function useGetHorario() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async () => {
    loading.value = true
    error.value = null

    try {
      data.value = await getHorarioService()
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se pudo crear el horario'
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

export function useAsignarPersonal() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (id, body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await asignarPersonalService(id, body)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se pudo crear el horario'
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

export function useDesasignarPersonal() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (id, body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await desasignarPersonalService(id, body)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se pudo crear el horario'
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
