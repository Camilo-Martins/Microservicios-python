import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    authId: localStorage.getItem('user_id') != null ? localStorage.getItem('user_id') : null,
    authNombre:localStorage.getItem('user_nombre') != null ? localStorage.getItem('user_nombre') : null,
    authToken: localStorage.getItem('user_token') != null ? localStorage.getItem('user_token') : null,
    authTienda: localStorage.getItem('user_tienda') != null ? localStorage.getItem('user_tienda') : null,
  }),

  actions: {
    iniciarSesion(data) {
      // Guardar en store
      localStorage.setItem('user_id', data.id);
      localStorage.setItem('user_nombre', data.nombre);
      localStorage.setItem('user_token', data.token);
      localStorage.setItem('user_tienda', data.nombre_tienda);
    },

    estasLogueado() {
      // Si no hay token → redirigir
      if (this.authId == null) {
        window.location.href = '/';
        return false;
      }

      // Sincronizar con localStorage
      this.authId = localStorage.getItem('user_id');
      this.authNombre = localStorage.getItem('user_nombre');
      this.authToken = localStorage.getItem('user_token');
      this.authTienda = localStorage.getItem('user_tienda');

      return true;
    },

    cerrarSesion() {
      if (window.confirm('¿Realmente desea cerrar sesión?')) {
        // Limpiar store
        this.id = null;
        this.nombre = null;
        this.token = null;
         this.nombre_tienda = null;

        // Limpiar localStorage
        localStorage.removeItem('user_id');
        localStorage.removeItem('user_nombre');
        localStorage.removeItem('user_token');
        localStorage.removeItem('user_tienda');
        
        window.location.href = '/inicio-sesion';
      }
    },
  },
});