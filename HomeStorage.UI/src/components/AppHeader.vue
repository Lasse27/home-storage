<script lang="ts" setup>

</script>

<template>
    <div class="app-header">
         <div class="header-body">
            <div class="header-section">
                <h1 class="app-title">HomeStorage</h1>
            </div>
            <div class="header-section">
                <button>Mode</button>
                <button>Settings</button>
            </div>
         </div>
    </div>
</template>

<style scoped>
.app-header {
    width: 100%;
    background-color: var(--surface);
    box-shadow: var(--shadow-sm);
    padding: 0.25rem;
    display: flex;
    justify-content: center;
    border-bottom: 1px solid var(--border);
    box-sizing: border-box;
}
.header-body {
    gap: 2rem;
    width: 100%;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
}
.header-section {
    display: flex;
    align-items: center;
    gap: 1rem;
}
</style>