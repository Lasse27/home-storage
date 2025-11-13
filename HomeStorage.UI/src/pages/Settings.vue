<script lang="ts" setup>
import Dialog from '@/components/Dialog.vue';
import PageHeader from '@/components/PageHeader.vue';
import { Home, Folder, Settings, Info, CloudDownload } from 'lucide-vue-next'
import { ref } from 'vue';

const popup_dialog = ref<typeof Dialog>();

</script>

<template>
    <div class="home-page">
        <PageHeader title="Einstellungen" :icon="Settings" />
        <Dialog ref="popup_dialog"></Dialog>
        <button @click=""></button>
    </div>
</template>

<style scoped>
.home-page {
    height: 100%;
    width: 100%;
    box-sizing: border-box;
}
</style>