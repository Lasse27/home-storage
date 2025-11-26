<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import * as system from '@/services/system'
import * as system_types from '@/types/system';
import ProgressCircle from '@/components/common/ProgressCircle.vue';
import { round } from '@/services/math_helpers';
import CpuPanelFreqs from '@/components/SystemOverview/CpuPanel/CpuPanelFreqs.vue';


const cpuData = ref<system_types.SystemCpuResponse>(system_types.defaultSystemCpuResponse());
const cpuLoading = ref(false);
const cpuError = ref<unknown>(null);
const cpuFreqs_avg = ref<system_types.CpuFreqResponse>(system_types.defaultCpuFreqResponse())
const cpuPercs_avg = ref<number>(0);

/** Fetches cpu data from /api/system/cpu */
async function fetchCpuData() {
    cpuError.value = null;
    cpuLoading.value = true;
    try {
        cpuData.value = await system.fetchCpuInfo()
        cpuFreqs_avg.value = system.generateAverageCpuFreqs(cpuData.value.cpu_freqs)
        cpuPercs_avg.value = round(system.generateAverageCpuPercs(cpuData.value.cpu_percs), 1)
    } catch (err) {
        cpuError.value = err;
    } finally {
        cpuLoading.value = false;
    }
}


const memoryData = ref<system_types.SystemMemoryResponse>(system_types.defaultSystemMemoryResponse());
const memoryLoading = ref(false);
const memoryError = ref<unknown>(null);

/** Fetches cpu data from /api/system/cpu */
async function fetchMemoryData() {
    memoryError.value = null;
    memoryLoading.value = true;
    try {
        memoryData.value = await system.fetchMemoryInfo()
    } catch (err) {
        memoryError.value = err;
    } finally {
        memoryLoading.value = false;
    }
}


const diskData = ref<system_types.SystemDiskResponse>(system_types.defaultSystemDiskResponse());
const diskLoading = ref(false);
const diskError = ref<unknown>(null);

/** Fetches disk data from /api/system/disk */
async function fetchDiskData() {
    diskError.value = null;
    diskLoading.value = true;
    try {
        diskData.value = await system.fetchDiskInfo()
    } catch (err) {
        diskError.value = err;
    } finally {
        diskLoading.value = false;
    }
}

/** Executes on mount of component. */
onMounted(() => {
    fetchCpuData();
    fetchMemoryData();
    fetchDiskData();
})


</script>

<template>
    <div class="panel">
        <h1>Systemüberblick</h1>
        <div class="panel-body">
            <div>
                <h2>CPU Auslastung</h2>
                <div class="cpu-section-content">
                    <ProgressCircle :percent="cpuPercs_avg" />
                    <CpuPanelFreqs :current="cpuFreqs_avg.current" :min="cpuFreqs_avg.min" :max="cpuFreqs_avg.max" />
                </div>
            </div>
            <div>
                <h2>Arbeitsspeicher Auslastung</h2>
                <div class="memory-section-content">
                    <div>
                        <h3> Virtual</h3>
                        <ProgressCircle :percent="memoryData.virtual.percent" />
                    </div>
                    <div>
                        <h3> Swap</h3>
                        <ProgressCircle :percent="memoryData.swap.percent" />
                    </div>
                </div>
            </div>
            <div>
                <h2>Partitionen Auslastung</h2>
                <div class="disk-section-content">
                    <div v-for="partition in diskData.usage">
                        <h3> Gerät: {{ partition.device }}</h3>
                        <ProgressCircle :percent="partition.percent" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.cpu-section-content {
    display: grid;
    grid-template-columns: 33% 1fr;
    gap: 2.5rem;
    padding: 1rem;
}

.memory-section-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5rem;
    padding: 1rem;
}

.disk-section-content {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5rem;
    padding: 1rem;
}
</style>