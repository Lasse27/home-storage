<script setup lang="ts">
// Methods
import { ref, onMounted } from 'vue';
import * as system from '@/services/system'
import * as system_types from '@/types/system';
import { round } from '@/services/math_helpers';
import ProgressCircle from '../common/ProgressCircle.vue';


// Var
const data = ref<system_types.SystemDiskResponse>(system_types.defaultSystemDiskResponse());
const usage = ref<system_types.DiskUsageResponse[]>([])
const loading = ref(false);
const error = ref<unknown>(null);


/** Fetches cpu data from /api/system/cpu */
async function fetchData() {
    error.value = null;
    loading.value = true;
    try {
        data.value = await system.fetchDiskInfo()
        usage.value = data.value.usage;
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
        <h1> Laufwerke </h1>

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
            <div class="disk-circle-panel-group">
                <div v-for="value in usage">
                    <h2> Partition: {{ value.device }}</h2>
                    <div class="disk-circle-panel">
                        <ProgressCircle :percent="value.percent" />
                        <table>
                            <thead>
                                <tr>
                                    <th>Area</th>
                                    <th>Wert MB</th>
                                    <th>Wert GB</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td> Gesamt</td>
                                    <td>{{ round(value.total / 1024 / 1024, 2) }}MB</td>
                                    <td>{{ round(value.total / 1024 / 1024 / 1024, 2) }}GB</td>
                                </tr>
                                <tr>
                                    <td> Frei</td>
                                    <td>{{ round(value.free / 1024 / 1024, 2) }}MB</td>
                                    <td>{{ round(value.free / 1024 / 1024 / 1024, 2) }}GB</td>
                                </tr>
                                <tr>
                                    <td> Genutzt</td>
                                    <td>{{ round(value.used / 1024 / 1024, 2) }}MB</td>
                                    <td>{{ round(value.used / 1024 / 1024 / 1024, 2) }}GB</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style lang="css" scoped>
.disk-circle-panel-group {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
}

.disk-circle-panel {
    display: grid;
    grid-template-columns: 33% auto;
    gap: 1rem;
}
</style>