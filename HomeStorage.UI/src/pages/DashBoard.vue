<script lang="ts" setup>
import PageHeader from '@/components/PageHeader.vue';
import { Home, Folder, Settings, Info, CloudDownload } from 'lucide-vue-next'
</script>

<template>
    <div class="home-page">
        <PageHeader title="Dashboard" :icon="Home" />
    </div>
</template>

<style scoped>
.home-page {
    height: 100%;
    width: 100%;
    box-sizing: border-box;
}
</style>