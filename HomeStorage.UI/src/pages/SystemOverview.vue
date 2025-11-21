<script lang="ts" setup>
import PageHeader from '@/components/PageHeader.vue';
import CpuPanel from '@/components/SystemOverview/CpuPanel.vue';
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
    overflow: scroll;
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



/* ------------------------- */
/* HÜBSCHERE TABELLE */
/* ------------------------- */

</style>