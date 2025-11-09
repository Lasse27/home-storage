<script setup lang="ts">
import AppFooter from './components/AppFooter.vue';
import AppHeader from './components/AppHeader.vue';
import AppSidebar from './components/AppSidebar.vue';
import HomePage from './pages/HomePage.vue';

</script>

<template>
  <div class="app">
    <AppHeader style="grid-area: header;" />
    <AppSidebar style="grid-area: sidebar;" />
    <HomePage style="grid-area: main;" />
    <AppFooter style="grid-area: footer;" />
  </div>
</template>

<style scoped>
.app {
  display: grid;
  grid-template-rows: auto 1fr auto;
  grid-template-columns: 15vw 1fr;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  height: 100vh;
  width: 100vw;
}
</style>
