// services/registerService.ts
export async function addPersonal(body) {
  const token = localStorage.getItem('user_token')
  const response = await fetch(
    `${import.meta.env.VITE_API_HR_URL}personal/agregar`,
    {
      method: 'POST',
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
