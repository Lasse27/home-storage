<script setup lang="ts">
import { round } from '@/services/math_helpers';

const props = defineProps({
    total: { type: Number, default: 0 },
    used: { type: Number, default: 0 },
    free: { type: Number, default: 0 },
    percent: { type: Number, default: 0 },
    sin: { type: Number, default: 0 },
    sout: { type: Number, default: 0 },
})

</script>

<template>
    <table>
        <thead>
            <tr>
                <th>Speicherraum</th>
                <th>Zugewiesen (MB)</th>
                <th>Zugewiesen (GB)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> Gesamt </td>
                <td> {{ round(props.total / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.total / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Genutzt </td>
                <td> {{ round(props.used / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.used / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Frei </td>
                <td> {{ round(props.free / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.free / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Eingeswappte Bytes </td>
                <td> {{ round(props.sin / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.sin / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Ausgeswappte Bytes </td>
                <td> {{ round(props.sout / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.sout / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
        </tbody>
    </table>
</template>