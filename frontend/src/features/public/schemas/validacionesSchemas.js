import * as yup from 'yup';

export const registroSchema = yup.object({
    nombre: yup
        .string()
        .required('El campo nombre es obligatorio')
        .min(4, 'Ingrese nombre válido')
        .max(20, 'Ingrese nombre válido')
        .matches(/^[a-zA-Z0-9 ]+$/,'Solo se permiten letras, números y espacios')
        ,
    nombre_tienda: yup
        .string()
        .required('El campo nombre tienda es obligatorio')
        .min(6, 'Ingrese nombre tienda válido')
        .matches(/^[a-zA-Z0-9 ]+$/,'Solo se permiten letras, números y espacios')
        .max(20, 'Ingrese nombre tienda  válido'),
    email: yup
        .string()
        .required('El campo email es obligatorio')
        .email('El email ingresado no es válido')
        .min(10, 'Ingrese email válido')
        .matches(/^[^\s@]+@[^\s@]+\.[^\s@]+$/,'Nombre no valido')
        .max(50, 'Ingrese email válido'),
    password: yup
        .string()
        .required('El campo Contraseña es obligatorio')
        .min(8, 'La contraseña debe tener 8 caracteres minimo.')
        .max(20, 'La contraseña debe tener 20 caracteres maximo')
        .matches(/[a-z]/, 'Debe contener una letra minúscula')
        .matches(/[A-Z]/, 'Debe contener una letra mayúscula')
        .matches(/\d/, 'Debe contener un número')
        .test(
          'no-control-chars',
          'Formato inválido',
          value => !/[\u0000-\u001F\u007F]/.test(value))
        ,
});

export const loginSchema = yup.object({
  email: yup
    .string()
    .required('El campo E-Mail es obligatorio')
    .email('El E-Mail ingresado no es válido')
    .matches(/^[^\s@]+@[^\s@]+\.[^\s@]+$/,'Nombre no valido')
    .min(10, 'Ingrese email válido')
    .max(50, 'Ingrese email válido'),
  password: yup.string().required('El campo Contraseña es obligatorio'),
});

export const resetSchema = yup.object({
  email: yup
    .string()
    .required('El campo E-Mail es obligatorio')
    .email('El E-Mail ingresado no es válido')
    .matches(/^[^\s@]+@[^\s@]+\.[^\s@]+$/,'Nombre no valido')
    .min(10, 'Ingrese email válido')
    .max(50, 'Ingrese email válido'),
  password: yup.string().required('El campo Contraseña es obligatorio'),
});

export const passwordSchema = yup.object({
  password: yup
    .string()
    .required('El campo Contraseña es obligatorio')
    .min(8, 'La contraseña debe tener 8 caracteres minimo.')
    .max(20, 'La contraseña debe tener 20 caracteres maximo')
    .matches(/[a-z]/, 'Debe contener una letra minúscula')
    .matches(/[A-Z]/, 'Debe contener una letra mayúscula')
    .matches(/\d/, 'Debe contener un número')
    .test(
      'no-control-chars',
      'Formato inválido',
      value => !/[\u0000-\u001F\u007F]/.test(value))
  ,
});