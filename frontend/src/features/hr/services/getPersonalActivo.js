// services/registerService.ts
export async function obtenerPersonalActivo() {
  const token = localStorage.getItem('user_token')
  const response = await fetch(`${import.meta.env.VITE_API_HR_URL}personal/personal-activo`, {
    method: 'GET',
    headers: {
      'content-type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(),
  })

  const data = await response.json()

  if (!response.ok) {
    throw {
      status: response.status,
      data,
    }
  }

  return data.data
}
