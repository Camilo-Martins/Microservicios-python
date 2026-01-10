import { createRouter, createWebHistory } from 'vue-router'

import PublicLayout from '@/layouts/PublicLayout.vue'

import LoginView from '@/features/public/views/LoginView.vue'
import Register from '@/features/public/views/Register.vue'
import ResetPasswordView from '@/features/public/views/ResetPasswordView.vue'
import NewPasswordView from '@/features/public/views/NewPasswordView.vue'



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
          path: '/reset-password',
          name: 'reset-password',
          component: ResetPasswordView,
        },
          {
          path: '/change-password',
          name: '/change-password',
          component: ResetPasswordView,
        },
      ],
    },
  ],
})

export default router
