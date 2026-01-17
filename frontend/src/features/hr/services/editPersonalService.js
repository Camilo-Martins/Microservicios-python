// services/registerService.ts
export async function editPersonalServive(id, body) {
  const token = localStorage.getItem('user_token')
  console.log(token)
  const response = await fetch(
    `${import.meta.env.VITE_API_HR_URL}personal/editar/${id}`,
    {
      method: 'PUT',
      headers: { 
        'content-type': 'application/json',
       'Authorization': `Bearer ${token}` },
      body: JSON.stringify(body),
    }
  );

   const data = await response.json()

  if (!response.ok) {
     throw {
      status: response.status,
      data,
    }
  }

  return data;
}
