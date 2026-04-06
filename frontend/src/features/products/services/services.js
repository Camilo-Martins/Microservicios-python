export async function addProducto(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}productos/agregar`, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(body),
  })

  const data = await response.json()

  if (!response.ok) {
    throw {
      status: response.status,
      data,
    }
  }

  return data
}

export async function getProductos(params = {}) {
  const token = localStorage.getItem('user_token')

  const query = new URLSearchParams()

  if (params.proveedor) {
    query.append('proveedor', params.proveedor)
  }

  if (params.categoria) {
    query.append('categoria', params.categoria)
  }

  const queryString = query.toString()
  const url = `${import.meta.env.VITE_API_STORE_URL}productos/obtener/${
    queryString ? `?${queryString}` : ''
  }`

  const response = await fetch(url, {
    method: 'GET',
    headers: {
      'content-type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
  })

  const data = await response.json()

  if (!response.ok) {
    throw {
      status: response.status,
      data,
    }
  }

  return data
}

export async function editProducto(id, body) {
  const token = localStorage.getItem('user_token')

  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}productos/editar/${id}`, {
    method: 'PUT',
    headers: {
      'content-type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(body),
  })

  const data = await response.json()

  if (!response.ok) {
    throw {
      status: response.status,
      data,
    }
  }

  return data
}
