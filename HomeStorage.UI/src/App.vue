<script setup lang="ts">
import AppSidebar from './components/AppSidebar.vue';
import HomePage from './pages/HomePage.vue';

</script>

<template>
  <div class="app">
    <AppSidebar style="grid-area: sidebar; z-index: 99;" />
    <HomePage style="grid-area: main; z-index: 99;" />
    <AppFooter style="grid-area: footer; z-index: 100;" />
  </div>
</template>

<style scoped>
.app {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 15vw 1fr;
  grid-template-areas:
    "sidebar main";
  height: 100vh;
  width: 100vw;
  background-color: var(--surface-50);
}
</style>
