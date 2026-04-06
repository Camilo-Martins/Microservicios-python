import * as yup from 'yup'

export const personalSchema = yup.object({
  nombre_completo: yup
    .string()
    .required('*El campo nombre es obligatorio/ ')
    .min(4, '*Ingrese nombre válido/ ')
    .max(20, '*Ingrese nombre válido/ ')
    .matches(/^[a-zA-Z0-9 ]+$/, '*Solo se permiten letras, números y espacios/ '),
  rut: yup
    .string()
    .min(9, '*Ingrese Rut válido EJ: 11.111.111-1/ ')
    .matches(/^(?:\d{1,3}(?:\.\d{3}){2}-[\dkK]|\d{7,9}[\dkK]?)$/, '*Formato de RUT inválido/ ')
    .max(12, '*Ingrese Rut válido EJ: 11.111.111-1/ '),
  telefono: yup
    .string()
    .required('*El campo teléfono es obligatorio/ ')
    .min(8, '*Ingrese teléfono válido  +1234567890, 1234567890 O 12345678/ ')
    .max(15, '*Ingrese teléfono válido  +1234567890 o 1234567890/ ')
    .matches(/^[0-9]+$/, '*Ingrese teléfono válido  +1234567890 o 1234567890/ ')
    .matches(/^[\+]?[0-9]{7,15}$/, '*Formato válido: +1234567890 o 1234567890/ '),
  pago_diario: yup
    .string()
    .matches(/[0-9]{1,4}$/, '*Ingrese un formato de pago válido, por ejemplo: $20000 o 20000'),
})
