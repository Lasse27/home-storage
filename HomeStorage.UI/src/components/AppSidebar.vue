<script lang="ts" setup>
import { ref } from 'vue'
import { Home, Folder, Settings, Info, CloudDownload } from 'lucide-vue-next'

const activeItem = ref('home')

const navItems = [
  { id: 'home', label: 'Dashboard', icon: Home },
  { id: 'files', label: 'Dateien', icon: Folder },
  { id: 'settings', label: 'Einstellungen', icon: Settings },
  { id: 'about', label: 'Über', icon: Info },
]

const setActive = (id: string) => {
  activeItem.value = id
}
</script>

<template>
  <aside class="sidebar">
    <header>
      <component :is="CloudDownload"/>
      <span> HomeStorage </span>
    </header>

    <nav class="sidebar-nav">
        <button v-for="item in navItems" :key="item.id" class="sidebar-nav-button nav-button" :class="{ 'active': activeItem === item.id }" @click="setActive(item.id)">
          <component :is="item.icon"/>
          <span>{{ item.label }}</span>
        </button>
    </nav>
    <footer class="sidebar-footer">
      <small>100 GB Free Storage</small>
    </footer>
    <footer class="sidebar-footer">
      <small>© 2024 HomeStorage</small><br />
      <small>Made with ♥ by Lasse</small><br />
      <small>v1.0.0</small>
    </footer>
  </aside>
</template>

<style scoped>
.sidebar {
  /* Size */
  width: 100%;
  height: 100%;
  box-sizing: border-box;

  /* Display */
  display: flex;
  flex-direction: column;

  /* Styling */
  background-color: var(--clr-surface-a10);
  border-right: 4px solid var(--clr-primary-a0);
}


.sidebar header {
  /* Size */
  width: 100%;
  padding: 2rem 1rem;
  box-sizing: border-box;

  /* Display */
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;

  font-weight: 500;
  font-size: 2rem;
  color: var(--clr-primary-a10);
  margin: 0;
}


.sidebar .sidebar-nav {
  /* Size */
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  flex-grow: 1;
  box-sizing: border-box;
}


.sidebar-nav-button {
  /* Size */
  padding: 0.75rem 1rem;
  box-sizing: border-box;
  cursor: pointer;
  width: 100%;

  /* Display */
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 1rem;

  /* Styling */
  font-size: 1rem;
  font-weight: 600;
  list-style: none;
  color: var(--clr-light-a0);
  background-color: var(--clr-surface-a20);
  border-radius: 0.75rem;
}

.sidebar-nav-button.active {
  background-color: var(--clr-primary-a10);
}

.sidebar-footer {
  /* Size */
  width: 100%;
  padding: 1rem;
  box-sizing: border-box;

  /* Display */
  text-align: center;

  font-size: 1rem;
  color: var(--clr-light-a0);
  border-top: 1px solid var(--clr-surface-a30);
}
</style>
