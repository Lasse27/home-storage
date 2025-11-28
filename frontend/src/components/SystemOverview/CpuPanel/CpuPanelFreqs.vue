<script setup lang="ts">
const props = defineProps({
    current: Number,
    min: Number,
    max: Number,
})

</script>

<template>
    <table>
        <thead>
            <tr>
                <th>Frequenz</th>
                <th>Wert</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> Aktuelle Frequenz</td>
                <td>{{ props.current }} MHz</td>
            </tr>
            <tr>
                <td> Minimale Frequenz</td>
                <td>{{ props.min }} MHz</td>
            </tr>
            <tr>
                <td> Maximale Frequenz</td>
                <td>{{ props.max }} MHz</td>
            </tr>
        </tbody>
    </table>
</template>