<script lang="ts" setup>
import PageHeader from '@/components/PageHeader.vue';
import CpuPanel from '@/components/system_overview/CpuPanel.vue';
import { Info } from 'lucide-vue-next'

</script>

<template>
    <div class="system-page">
        <PageHeader title="System" :icon="Info" style="grid-area: header;" />
        <div class="panel-container">
            <CpuPanel/>

            <div class="panel" style="grid-area: memory;">
                <h1> Memory </h1>

            </div>

            <div class="panel" style="grid-area: disk;">
                <h1> Disk </h1>

            </div>
        </div>
    </div>
</template>

<style scoped>
.system-page {
    height: 100%;
    width: 100%;
    box-sizing: border-box;

    display: flex;
    flex-direction: column;
}

.system-page .panel-container {
    height: 100%;
    width: 100%;
    box-sizing: border-box;

    padding: 1rem;
    gap: 1rem;

    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-areas: "cpu memory disk";
}

.system-page .panel {
    height: 100%;
    width: 100%;
    background-color: var(--clr-surface-a10);
    border: 2px solid var(--clr-surface-a20);
    border-radius: 0.5rem;
    padding: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.system-page .panel h1 {
    width: 100%;
    font-size: 1.25rem;
    background-color: var(--clr-surface-a20);
    border: 2px solid var(--clr-surface-a30);
    border-radius: 0.5rem;
    padding: 0.25rem;
    margin: 0;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
}

.system-page .panel h2 {
    width: 100%;
    font-size: 1rem;
    padding: 0.5rem 0.25rem;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    border-bottom: 2px solid var(--clr-surface-a20);
    margin-bottom: 0.5rem;
}

/* ------------------------- */
/* HÜBSCHERE TABELLE */
/* ------------------------- */

</style>