// services/registerService.ts
export async function resetPassword(body) {
  const response = await fetch(
    `${import.meta.env.VITE_API_URL}auth/recuperar-password`,
    {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
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
