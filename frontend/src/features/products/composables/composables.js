import { ref, readonly } from 'vue'
import { addProducto, getProductos, editProducto } from '../services/services'

export function useAddProducto() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await addProducto(body)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se pudo agregar el producto'
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

export function useGetProductos() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (params) => {
    loading.value = true
    error.value = null

    try {
      data.value = await getProductos(params)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se obtenieron los productos'
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

export function useEditProducto() {
  const data = ref(null)
  const loading = ref(false)
  const error = ref(null)

  const sendData = async (id, body) => {
    loading.value = true
    error.value = null

    try {
      data.value = await editProducto(id, body)
    } catch (e) {
      if (e?.data?.message) {
        error.value = e.data.message
      } else {
        error.value = 'No se pudo editar el producto'
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
