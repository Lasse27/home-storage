<script setup lang="ts">
import AppSidebar from './components/AppSidebar.vue';
import HomePage from './pages/DashBoard.vue';

</script>

<template>
  <div class="app">
    <AppSidebar style="grid-area: sidebar; z-index: 99;" />
    <RouterView/>
  </div>
</template>

<style scoped>
.app {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 17.5vw 1fr;
  grid-template-areas:
    "sidebar main";
  height: 100vh;
  width: 100vw;
  background-color: var(--clr-surface-a0);
  color: var(--clr-light-a0);
}
</style>
