import * as yup from 'yup'

export const productSchema = yup.object({
  nombre_producto: yup
    .string()
    .required('*El campo nombre es obligatorio/ ')
    .min(2, '*Ingrese nombre válido/ ')
    .max(50, '*Ingrese nombre válido/ ')
    .matches(/^[a-zA-Z0-9 ]+$/, '*Solo se permiten letras, números y espacios/ '),
  precio: yup
    .string()
    .matches(/[0-9]{1,4}$/, '*Ingrese precio válido, por ejemplo: $20000 o 20000'),
  stock: yup.string().matches(/[0-9]{1,4}$/, '*Ingrese un stock válido, por ejemplo: 20'),
})
