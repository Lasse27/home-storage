<script setup lang="ts">
// Methods
import { ref, onMounted } from 'vue';
import * as system from '@/services/system'
import * as system_types from '@/types/system';
import { round } from '@/services/math_helpers';
// Vue Components
import CpuPanelLoad from '@/components/SystemOverview/CpuPanel/CpuPanelLoad.vue';
import CpuPanelStats from '@/components/SystemOverview/CpuPanel/CpuPanelStats.vue';
import CpuPanelTimes from '@/components/SystemOverview/CpuPanel/CpuPanelTimes.vue';
import CpuPanelFreqs from '@/components/SystemOverview/CpuPanel/CpuPanelFreqs.vue';
import ProgressCircle from '@/components/common/ProgressCircle.vue';


// Var
const data = ref<system_types.SystemCpuResponse>(system_types.defaultSystemCpuResponse());
const times_avg = ref<system_types.CpuTimesResponse>(system_types.defaultCpuTimesResponse());
const freqs_avg = ref<system_types.CpuFreqResponse>(system_types.defaultCpuFreqResponse())
const percs_avg = ref<number>(0);
const loading = ref(false);
const error = ref<unknown>(null);


/** Fetches cpu data from /api/system/cpu */
async function fetchData() {
    error.value = null;
    loading.value = true;
    try {
        data.value = await system.fetchCpuInfo()
        times_avg.value = system.generateAverageCpuTimes(data.value.cpu_times)
        freqs_avg.value = system.generateAverageCpuFreqs(data.value.cpu_freqs)
        percs_avg.value = round(system.generateAverageCpuPercs(data.value.cpu_percs), 1)
    } catch (err) {
        error.value = err;
    } finally {
        loading.value = false;
    }
}

/** Executes on mount of component. */
onMounted(() => {
    fetchData();
})

</script>


<template>
    <div class="panel" style="grid-area: cpu;">
        <h1> CPU </h1>

        <!-- Display while the api is being fetched -->
        <div v-if="loading"
            style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-top: 1rem;">
            <h3>
                Daten werden geladen ...
            </h3>
        </div>

        <!-- Display if error occured while fetching -->
        <div v-else-if="error"
            style="display: flex; justify-content: center; align-items: center; flex-direction: column;  margin-top: 1rem;">
            <h3>
                Fehler:
            </h3>
            {{ error }}
        </div>


        <!-- Normal display -->
        <div v-else-if="data !== null" class="panel-body">

            <h2>Auslastung in Prozent</h2>
            <div class="cpu-circle-panel">
                <ProgressCircle :percent="percs_avg" />
                <CpuPanelFreqs :current="freqs_avg.current" :min="freqs_avg.min" :max="freqs_avg.max" />
            </div>

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


<style lang="css" scoped>
.cpu-circle-panel {
    display: grid;
    grid-template-columns: 25% 1fr;
    grid-template-rows: auto;
    gap: 1rem;
}

</style>