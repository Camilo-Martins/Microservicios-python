import { createRouter, createWebHistory } from 'vue-router'

import PublicLayout from '@/layouts/PublicLayout.vue'

import LoginView from '@/features/public/views/LoginView.vue'
import Register from '@/features/public/views/Register.vue'
import ResetPasswordView from '@/features/public/views/ResetPasswordView.vue'
import NewPasswordView from '@/features/public/views/NewPasswordView.vue'
import ConfirmAccount from '@/features/public/views/ConfirmAccount.vue'
import Error404 from '@/features/public/views/Error404.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      component: PublicLayout,
      children: [
        {
          path: '/login',
          name: 'login',
          component: LoginView,
        },
            {
          path: '/register',
          name: 'register',
          component: Register,
        },
             {
          path: '/confirmar-cuenta/:token',
          name: 'confirmar-cuenta',
          component: ConfirmAccount,
        },
            {
          path: '/reset-password',
          name: 'reset-password',
          component: ResetPasswordView,
        },
          {
          path: '/change-password/:token',
          name: '/change-password',
          component: NewPasswordView,
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

export default router
