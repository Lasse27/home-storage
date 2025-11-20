<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { fetchCpuInfo } from '@/services/system'
import { defaultCpuTimesResponse, defaultSystemCpuResponse, type CpuTimesResponse, type SystemCpuResponse } from '@/types/system';
import { round } from '@/services/math_helpers';
import CpuPanelLoad from './CpuPanelLoad.vue';
import CpuPanelStats from './CpuPanelStats.vue';
import CpuPanelTimes from './CpuPanelTimes.vue';
import { generateAverageCpuTimes } from '@/services/system';

const data = ref<SystemCpuResponse>(defaultSystemCpuResponse());
const times_avg = ref<CpuTimesResponse>(defaultCpuTimesResponse())
const loading = ref(false);
const error = ref<unknown>(null);

// Fetches cpu data from /api/system/cpu
async function fetchData() {
    error.value = null;
    loading.value = true;


    try {
        data.value = await fetchCpuInfo()
        times_avg.value = generateAverageCpuTimes(data.value.cpu_times)
    } catch (err) {
        error.value = err;
    } finally {
        loading.value = false;
    }
}


onMounted(() => {
    fetchData();
})

</script>

<template>
    <div class="panel" style="grid-area: cpu;">
        <h1> CPU </h1>
        <div v-if="loading"
            style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-top: 1rem;">
            <h3>
                Daten werden geladen ...
            </h3>
        </div>
        <div v-else-if="error"
            style="display: flex; justify-content: center; align-items: center; flex-direction: column;  margin-top: 1rem;">
            <h3>
                Fehler:
            </h3>
            {{ error }}
        </div>
        <div v-else-if="data !== null">
            
            <h2>Task Auslastung in Prozent %</h2>
            <CpuPanelLoad :min_1_load="round(data.cpu_load.min_1_load, 3)"
                :min_5_load="round(data?.cpu_load.min_5_load, 3)" :min_15_load="round(data?.cpu_load.min_15_load, 3)" />

            <h2>CPU Statistiken</h2>
            <CpuPanelStats :ctx_switches="round(data.cpu_stats.ctx_switches, 3)"
                :interrupts="round(data.cpu_stats.interrupts, 3)"
                :soft_interrupts="round(data.cpu_stats.soft_interrupts, 3)"
                :syscalls="round(data.cpu_stats.syscalls, 3)" />

            <h2>CPU Times</h2>
            <CpuPanelTimes :user="times_avg.user" :nice="times_avg.nice" :system="times_avg.system"
                :idle="times_avg.idle" :iowait="times_avg.iowait" :irq="times_avg.irq" :softirq="times_avg.softirq"
                :steal="times_avg.steal" :guest="times_avg.guest" :guest_nice="times_avg.guest_nice"
                :interrupt="times_avg.interrupt" :dpc="times_avg.dpc" />
        </div>
    </div>
</template>

<style lang="css" scoped></style>