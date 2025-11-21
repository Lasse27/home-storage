<script lang="ts" setup>
import ProgressCircle from '@/components/common/ProgressCircle.vue';
import PageHeader from '@/components/PageHeader.vue';
import { Home } from 'lucide-vue-next'
</script>

<template>
    <div class="home-page">
        <PageHeader title="Dashboard" :icon="Home" />
        <div class="panel-container">
            <!-- Dashboard content goes here -->
            <div class="panel" style="grid-area: recently_added;">
                <div class="panel-header"> Zuletzt hinzugefügt </div>
            </div>
            <div class="panel" style="grid-area: quick_actions;">
                <div class="panel-header"> Schnellaktionen </div>
            </div>
            <div class="panel" style="grid-area: system;">
                <div class="panel-header"> System-Übersicht </div>
                <div style="width: 50%;">
                    <ProgressCircle :percent="88" :show-text="true"/>

                </div>
            </div>

        </div>
    </div>
</template>

<style scoped>
.home-page {
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.home-page .panel-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-areas:
        "recently_added system"
        "quick_actions system";
    grid-template-rows: 1fr 1fr;
    height: 100%;
    gap: 1.5rem;
    padding: 1.5rem;
    box-sizing: border-box;
}

.home-page .panel {
    background-color: var(--clr-surface-a10);
    border: 1px solid var(--clr-surface-a20);
    border-radius: 1rem;
    box-sizing: border-box;
}

.panel .panel-header {
    box-sizing: border-box;
    padding: 0.75rem;
    font-size: 1.25rem;
    width: 100%;
    align-items: center;
    text-align: center;
    background-color: var(--clr-surface-a30);
    border-radius: 1rem 1rem 0 0;
}
</style>