export async function getNota(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}notas/obtener`, {
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

// services/registerService.ts
export async function addNota(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}notas/agregar`, {
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

export async function editNota(id, body) {
  const token = localStorage.getItem('user_token')

  const response = await fetch(`${import.meta.env.VITE_API_STORE_URL}notas/editar/${id}`, {
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
