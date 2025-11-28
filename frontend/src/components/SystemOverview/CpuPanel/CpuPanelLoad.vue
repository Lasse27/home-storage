<script setup lang="ts">
const props = defineProps({
    min_1_load: Number,
    min_5_load: Number,
    min_15_load: Number,
})

</script>

<template>
    <table>
        <thead>
            <tr>
                <th>Intervall</th>
                <th>Wert</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> 1 Minute/n</td>
                <td>{{ props.min_1_load }} %</td>
            </tr>
            <tr>
                <td> 5 Minute/n</td>
                <td>{{ props.min_5_load }} %</td>
            </tr>
            <tr>
                <td> 15 Minute</td>
                <td>{{ props.min_15_load }} %</td>
            </tr>
        </tbody>
    </table>
</template>