<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const storeName = computed(() => {
  return localStorage.getItem('user_tienda') || 'Mi tienda'
})

const logout = () => {
  localStorage.clear()
  router.push('/login')
}

const isActive = (name) => route.name === name
</script>

<template>
  <nav class="border-t border-blue-800 bg-blue-900/90 text-white shadow-sm">
    <div class="max-w-7xl mx-auto px-8 py-4 flex items-center justify-between">
      <RouterLink to="/panel" class="nav-link px-5 hover:bg-white/20 transition px-3 py-1 rounded-md">
        <span class="text-base font-medium opacity-90 text-xl uppercase">
          {{ storeName }}
        </span>
      </RouterLink>

      <div class="flex items-center gap-2 text-sm font-bold capitalice">
        <RouterLink to="/panel/personal" class="nav-link px-5 hover:bg-white/20 transition px-3 py-1 rounded-md"
          :class="{ 'nav-active': isActive('personal') }">
          Gesión de Personal
        </RouterLink>

        <RouterLink to="/panel/proveedores" class="nav-link px-5 hover:bg-white/20 transition px-3 py-1 rounded-md"
          :class="{ 'nav-active': isActive('proveedor') }">
          Proveedores
        </RouterLink>

        <RouterLink to="/panel/productos" class="nav-link px-5 hover:bg-white/20 transition px-3 py-1 rounded-md"
          :class="{ 'nav-active': isActive('productos') }">
          Productos
        </RouterLink>

        <button @click="logout"
          class="ml-4 px-3 py-1 rounded-md bg-white/10 hover:bg-white/30 transition uppercase font-bold">
          Salir
        </button>
      </div>
    </div>
  </nav>
</template>
