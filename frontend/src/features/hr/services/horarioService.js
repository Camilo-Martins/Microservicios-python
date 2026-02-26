// services/registerService.ts
export async function addHorarioService(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_HR_URL}horario/crear`, {
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

export async function getHorarioService(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_HR_URL}horario/obtener-horario`, {
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

export async function asignarPersonalService(id, body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(
    `${import.meta.env.VITE_API_HR_URL}horario/asignacion-personal/${id}`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(body),
    },
  )

  const data = await response.json()

  if (!response.ok) {
    throw {
      status: response.status,
      data,
    }
  }

  return data
}

export async function desasignarPersonalService(id, body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(
    `${import.meta.env.VITE_API_HR_URL}horario/eliminacion-personal/${id}`,
    {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(body),
    },
  )

  const data = await response.json()

  if (!response.ok) {
    throw {
      status: response.status,
      data,
    }
  }

  return data
}
