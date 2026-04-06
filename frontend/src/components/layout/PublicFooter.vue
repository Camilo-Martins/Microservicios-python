<template>
  <footer class="border-t border-blue-800 bg-blue-900/90">
    <div
      class="mx-auto max-w-6xl px-6 py-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
    >
      <!-- Nombre del sistema -->
      <div class="text-center md:text-left">
        <p class="text-base font-semibold text-blue-100">Sistema de Gestión de Tiendas</p>
        <p class="text-xs text-blue-300">Plataforma administrativa</p>
      </div>

      <!-- Redes sociales -->
      <nav class="flex justify-center gap-4 text-sm text-blue-300">
        <a href="#" class="hover:text-white transition-colors"> GitHub </a>
        <a href="#" class="hover:text-white transition-colors"> LinkedIn </a>
        <a href="#" class="hover:text-white transition-colors"> YouTube </a>
      </nav>

      <!-- Copyright -->
      <div class="text-center md:text-right text-xs text-blue-300">
        © {{ new Date().getFullYear() }} Camilo Martins
        <span class="hidden md:inline">·</span>
        <span class="block md:inline">Todos los derechos reservados</span>
      </div>
    </div>
  </footer>
</template>
