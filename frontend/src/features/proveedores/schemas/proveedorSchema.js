import * as yup from 'yup'

export const proveedorSchema = yup.object({
  nombre_completo: yup
    .string()
    .required('*El Representante es obligatorio')
    .min(2, '*Nombre Representante mínimo 4 caracteres')
    .max(20, '*Nombre Representante máximo 20 caracteres')
    .matches(/^[a-zA-Z0-9 ]{2,20}$/, '*Solo se permiten letras, números y espacios'),
  nombre_empresa: yup
    .string()
    .required('*El campo nombre empresa es obligatorio')
    .min(2, '*Ingrese nombre empresa válido')
    .matches(/^[a-zA-Z0-9 ]+$/, '*Solo se permiten letras, números y espacios')
    .max(20, '*Ingrese nombre empresa válido'),
  telefono: yup
    .string()
    .required('*El campo teléfono es obligatorio')
    .matches(/^[\+]?[0-9]{7,15}$/, '*Formato válido: +1234567890 o 1234567890'),
})
