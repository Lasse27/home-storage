<script lang="ts" setup>
import ProgressCircle from '@/components/common/ProgressCircle.vue';
import QuickActions from '@/components/DashBoard/QuickActions.vue';
import RecentlyAdded from '@/components/DashBoard/RecentlyAdded.vue';
import SystemSummary from '@/components/DashBoard/SystemSummary.vue';
import PageHeader from '@/components/PageHeader.vue';
import { Home } from 'lucide-vue-next'
</script>

<template>
    <div class="home-page">
        <PageHeader title="Dashboard" :icon="Home" />
        <div class="panel-container">
            <!-- Dashboard content goes here -->
            <RecentlyAdded style="grid-area: recently_added;" />
            <SystemSummary style="grid-area: system;" />
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
        "recently_added system";
    height: 100%;
    gap: 1rem;
    padding: 1rem;
    box-sizing: border-box;
}
</style>