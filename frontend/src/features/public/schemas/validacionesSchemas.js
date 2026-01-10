import * as yup from 'yup';

export const registroSchema = yup.object({
    nombre: yup
        .string()
        .required('El campo nombre es obligatorio')
        .min(10, 'Ingrese nombre válido')
        .max(20, 'Ingrese nombre válido'),
    email: yup
        .string()
        .required('El campo email es obligatorio')
        .email('El email ingresado no es válido')
        .min(10, 'Ingrese email válido')
        .max(50, 'Ingrese email válido'),
    password: yup
        .string()
        .required('El campo Contraseña es obligatorio')
        .min(8, 'La contraseña debe tener 8 caracteres minimo.')
        .max(20, 'La contraseña debe tener 20 caracteres maximo'),
});

export const loginSchema = yup.object({
  email: yup
    .string()
    .required('El campo E-Mail es obligatorio')
    .email('El E-Mail ingresado no es válido')
    .min(10, 'Ingrese email válido')
    .max(50, 'Ingrese email válido'),
  password: yup.string().required('El campo Contraseña es obligatorio'),
});

export const confirmacionSchema = yup.object({
  password: yup
    .string()
    .required('El campo Contraseña es obligatorio')
    .min(8, 'La contraseña debe tener 8 caracteres minimo.')
    .max(20, 'La contraseña debe tener 20 caracteres maximo'),
});