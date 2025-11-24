<script setup lang="ts">
// Methods
import { ref, onMounted } from 'vue';
import * as system from '@/services/system'
import * as system_types from '@/types/system';
import { round } from '@/services/math_helpers';


// Var
const data = ref<system_types.SystemDiskResponse>(system_types.defaultSystemDiskResponse());
const loading = ref(false);
const error = ref<unknown>(null);


/** Fetches cpu data from /api/system/cpu */
async function fetchData() {
    error.value = null;
    loading.value = true;
    try {
        data.value = await system.fetchDiskInfo()
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


        </div>
    </div>
</template>


<style lang="css" scoped></style>