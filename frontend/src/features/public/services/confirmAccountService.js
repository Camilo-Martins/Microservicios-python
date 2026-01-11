// services/registerService.ts
export async function confirmAccoutn(token) {
  const response = await fetch(
    `${import.meta.env.VITE_API_URL}auth/confirmar-cuenta/${token}`,
    {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(),
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
