<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { fetchCpuInfo } from '@/services/system'
import type { SystemCpuResponse } from '@/types/system';
import { round } from '@/services/math_helpers';
import CpuPanelLoad from './CpuPanelLoad.vue';

const data = ref<SystemCpuResponse | null>(null);
const loading = ref(false);
const error = ref<unknown>(null);

// Fetches cpu data from /api/system/cpu
async function fetchData() {
    error.value = null;
    loading.value = true;

    try {
        data.value = await fetchCpuInfo()
    } catch (err) {
        error.value = err;
    } finally {
        loading.value = false;
    }
}

onMounted(() => fetchData())

</script>

<template>
    <div class="cpu-panel" style="grid-area: cpu;">
        <h1> CPU </h1>
        <div v-if="loading">Lade ...</div>
        <div v-else-if="error">Fehler: {{ error }}</div>
        <div v-else-if="data !== null">
            <h2>Task Auslastung in Prozent %</h2>
            <CpuPanelLoad :min_1_load="round(data?.cpu_load?.min_1_load, 3)"
                :min_5_load="round(data?.cpu_load?.min_5_load, 3)"
                :min_15_load="round(data?.cpu_load?.min_15_load, 3)" />


            <h2>CPU Statistiken</h2>
            <table class="sys-table">
                <thead>
                    <tr>
                        <th>Statistik</th>
                        <th>Wert</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td> ctx_switches</td>
                        <td>{{ round(data?.cpu_stats?.ctx_switches, 3) }}</td>
                    </tr>
                    <tr>
                        <td> interrupts</td>
                        <td>{{ round(data?.cpu_stats?.interrupts, 3) }}</td>
                    </tr>
                    <tr>
                        <td> soft_interrupts</td>
                        <td>{{ round(data?.cpu_stats?.soft_interrupts, 3) }}</td>
                    </tr>
                    <tr>
                        <td> syscalls</td>
                        <td>{{ round(data?.cpu_stats?.syscalls, 3) }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<style lang="css" scoped>
.cpu-panel {
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

.cpu-panel h1 {
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

.cpu-panel h2 {
    width: 100%;
    font-size: 1rem;
    padding: 0.5rem 0.25rem;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    border-bottom: 2px solid var(--clr-surface-a20);
    margin-bottom: 0.5rem;
    margin-top: 1rem;
}
</style>