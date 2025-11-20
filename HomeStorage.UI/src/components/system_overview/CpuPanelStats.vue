<script setup lang="ts">
import { round } from '@/services/math_helpers';

const props = defineProps({
    ctx_switches: Number,
    interrupts: Number,
    soft_interrupts: Number,
    syscalls: Number,
})

</script>

<template>
    <table>
        <thead>
            <tr>
                <th>Statistik</th>
                <th>Wert</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> ctx_switches</td>
                <td>{{ props.ctx_switches }}</td>
            </tr>
            <tr>
                <td> interrupts</td>
                <td>{{ props.interrupts }}</td>
            </tr>
            <tr>
                <td> soft_interrupts</td>
                <td>{{ props.soft_interrupts }}</td>
            </tr>
            <tr>
                <td> syscalls</td>
                <td>{{ props.syscalls }}</td>
            </tr>
        </tbody>
    </table>
</template>