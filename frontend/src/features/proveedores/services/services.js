export async function getProveedores(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}proveedores/obtener`, {
    method: 'GET',
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

export async function addProveedor(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}proveedores/agregar`, {
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

export async function editProveedor(id, body) {
  const token = localStorage.getItem('user_token')

  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}proveedores/editar/${id}`, {
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

export async function getProveedorLista(body) {
  const token = localStorage.getItem('user_token')

  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}proveedores/obtener/lista`, {
    method: 'GET',
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
