import { createRouter, createWebHistory } from 'vue-router'

import PublicLayout from '@/layouts/PublicLayout.vue'

import LoginView from '@/features/public/views/LoginView.vue'
import Register from '@/features/public/views/Register.vue'
import ResetPasswordView from '@/features/public/views/ResetPasswordView.vue'
import NewPasswordView from '@/features/public/views/NewPasswordView.vue'
import ConfirmAccount from '@/features/public/views/ConfirmAccount.vue'
import Error404 from '@/features/public/views/Error404.vue'
import Panel from '@/features/private/views/Panel.vue'
import { useAuthStore } from '@/stores/authStore'
import PrivateLayout from '@/features/private/components/PrivateLayout.vue'
import PersonalView from '@/features/hr/views/PersonalView.vue'
import PersonaView from '@/features/hr/views/PersonaView.vue'
import HorarioView from '@/features/hr/views/HorarioView.vue'
import Proveedor from '@/features/proveedores/Proveedor.vue'
import Productos from '@/features/products/Productos.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: PublicLayout,
      children: [
        {
          path: '',
          redirect: '/login',
        },
        {
          path: '/login',
          name: 'login',
          component: LoginView,
          meta: { guestOnly: true },
        },
        {
          path: '/register',
          name: 'register',
          component: Register,
          meta: { guestOnly: true },
        },
        {
          path: '/confirmar-cuenta/:token',
          name: 'confirmar-cuenta',
          component: ConfirmAccount,
          meta: { guestOnly: true },
        },
        {
          path: '/reset-password',
          name: 'reset-password',
          component: ResetPasswordView,
          meta: { guestOnly: true },
        },
        {
          path: '/change-password/:token',
          name: '/change-password',
          component: NewPasswordView,
          meta: { guestOnly: true },
        },
      ],
    },
    {
      path: '/panel',
      component: PrivateLayout,
      meta: {
        requiresAuth: true,
      },
      children: [
        {
          path: '/panel',
          name: 'panel',
          component: Panel,
        },
        {
          path: '/panel/personal',
          name: 'personal',
          component: PersonalView,
        },
        {
          path: '/panel/persona/:id',
          name: 'persona',
          component: PersonaView,
        },
        {
          path: '/panel/horario',
          name: 'horario',
          component: HorarioView,
        },
        {
          path: '/panel/productos',
          name: 'productos',
          component: Productos,
        },
        {
          path: '/panel/proveedores',
          name: 'proveedores',
          component: Proveedor,
        },
        {
          path: '/panel/ventas',
          name: 'ventas',
          component: HorarioView,
        },
      ],
    },

    {
      path: '/:pathMatch(.*)*',
      name: 'pagina-no-encontrada',
      component: Error404,
    },
  ],
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('user_token')

  // Usuario logeado intentando entrar a página pública
  if (token && to.meta.guestOnly) {
    return next('/panel')
  }

  // Usuario NO logeado intentando entrar a ruta protegida
  if (!token && to.meta.requiresAuth) {
    return next('/')
  }

  next()
})

export default router
