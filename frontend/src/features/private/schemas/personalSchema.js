import * as yup from 'yup';

export const personalSchema = yup.object({
    nombre_completo: yup
        .string()
        .required('El campo nombre es obligatorio')
        .min(4, 'Ingrese nombre válido')
        .max(20, 'Ingrese nombre válido')
        .matches(/^[a-zA-Z0-9 ]+$/,'Solo se permiten letras, números y espacios')
        ,
    rut: yup
        .string()
        .matches(/^\d{7,8}-[\dkK]$/,' Formato: 11111111-1')
        .required('RUT obligatorio'),
    telefono: yup
        .string()
        .matches(/^569\d{8}$/,' Formato: 569XXXXXXXX' )
        .required('Teléfono obligatorio')
});
