<script lang="ts" setup>

defineProps<{
    title: string;
    icon: any;
}>();
</script>

<template>
    <header class="page-header">
        <component :is="icon"/>
        <h1>{{ title }}</h1>
    </header>
</template>

<style scoped>

.page-header {
    padding: 0.25rem 1rem;
    border-bottom: 1px solid var(--clr-surface-a20);
    background-color: var(--clr-surface-a10);
    color: var(--clr-light-a0);
    box-sizing: border-box;
    
    /* Display */
    gap: 1rem;
    display: flex;
    flex-direction: row;
    align-items: center;
}

.page-header h1 {
    font-size: 1.5rem;
    font-weight: 500;
}

.page-header svg {
    width: 2rem;
    height: 2rem;
}
</style>