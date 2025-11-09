<script lang="ts" setup>
import { ref } from 'vue'
import { Home, Folder, Settings, Info } from 'lucide-vue-next'

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
    <header class="sidebar-header">
      <h2 class="app-title">HomeStorage</h2>
    </header>

    <nav class="sidebar-nav">
      <ul>
        <li
          v-for="item in navItems"
          :key="item.id"
          :class="{ active: activeItem === item.id }"
          @click="setActive(item.id)"
        >
          <component :is="item.icon" class="icon" />
          <span>{{ item.label }}</span>
        </li>
      </ul>
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
  display: flex;
  flex-direction: column;
  background-color: var(--surface-100);
  border-right: 1px solid var(--border);
  box-shadow: rgba(0, 0, 0, 0.08) 2px 0 6px;
  color: var(--text-color);
}

.sidebar-header {
  padding: 1.2rem 1rem;
  font-weight: 600;
  font-size: 1.2rem;
  border-bottom: 1px solid var(--border);
  text-align: center;
  background-color: var(--surface-200);
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
}

.sidebar-nav ul {
  list-style: none;
  margin: 0;
  padding: 0.5rem;
}

.sidebar-nav li {
  display: flex;
  align-items: center;
  padding: 0.7rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.sidebar-nav li:hover {
  background-color: var(--surface-hover);
}

.sidebar-nav li.active {
  background-color: var(--primary-light);
  color: var(--primary-color);
  font-weight: 600;
}

.icon {
  width: 20px;
  height: 20px;
  margin-right: 0.8rem;
}

.sidebar-footer {
  padding: 0.8rem;
  text-align: center;
  border-top: 1px solid var(--border);
  font-size: 0.85rem;
  color: var(--text-secondary);
}
</style>
