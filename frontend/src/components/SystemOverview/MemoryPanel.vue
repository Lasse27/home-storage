<script setup lang="ts">
// Methods
import { ref, onMounted } from 'vue';
import * as system from '@/services/system'
import * as system_types from '@/types/system';
// Vue Components
import MemoryPanelVirtual from './MemoryPanel/MemoryPanelVirtual.vue';
import MemoryPanelSwap from './MemoryPanel/MemoryPanelSwap.vue';
import ProgressCircle from '../common/ProgressCircle.vue';


// Var
const data = ref<system_types.SystemMemoryResponse>(system_types.defaultSystemMemoryResponse());
const loading = ref(false);
const error = ref<unknown>(null);


/** Fetches cpu data from /api/system/cpu */
async function fetchData() {
    error.value = null;
    loading.value = true;
    try {
        data.value = await system.fetchMemoryInfo()
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
        <h1> Memory </h1>

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

            <div class="memory-panel-header">
                <h2 style="grid-area: headerV;">Auslastung Virtual</h2>
                <ProgressCircle style="grid-area: virtualP; top: -1rem;" :percent="data.virtual.percent" />
                <h2 style="grid-area: headerS;">Auslastung Swap</h2>
                <ProgressCircle style="grid-area: swapP; top: -1rem;" :percent="data.swap.percent" />
            </div>

            <h2>Virtueller Speicher</h2>
            <MemoryPanelVirtual :total="data.virtual.total" :percent="data.virtual.percent" :used="data.virtual.used"
                :free="data.virtual.free" :active="data.virtual.active" :inactive="data.virtual.inactive"
                :buffers="data.virtual.buffers" :cached="data.virtual.cached" :shared="data.virtual.shared"
                :slab="data.virtual.slab" :wired="data.virtual.wired" />

            <h2>Swap Speicher</h2>
            <MemoryPanelSwap :total="data.swap.total" :used="data.swap.used" :free="data.swap.free"
                :percent="data.swap.percent" :sin="data.swap.sin" :sout="data.swap.sout" />
        </div>
    </div>
</template>

<style lang="css" scoped>
.memory-panel-header {
    width: 100%;
    display: grid;
    grid-template-columns: auto ;
    grid-template-rows: auto 10rem;
    grid-template-areas:
        "headerV headerS"
        "virtualP swapP";
    column-gap: 2rem;
    justify-content: center;
}
</style>