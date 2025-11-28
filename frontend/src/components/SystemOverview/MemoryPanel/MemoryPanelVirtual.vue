<script setup lang="ts">
import { round } from '@/services/math_helpers';
import { computed } from 'vue';

const props = defineProps({
    total: { type: Number, default: 0 },
    available: { type: Number, default: 0 },
    percent: { type: Number, default: 0 },
    used: { type: Number, default: 0 },
    free: { type: Number, default: 0 },
    active: { type: Number, default: 0 },
    inactive: { type: Number, default: 0 },
    buffers: { type: Number, default: 0 },
    cached: { type: Number, default: 0 },
    shared: { type: Number, default: 0 },
    slab: { type: Number, default: 0 },
    wired: { type: Number, default: 0 },
})

const propRows = computed(() => Object.entries(props).filter(([_, value]) => value !== undefined))

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
                <td> Verfügbar </td>
                <td> {{ round(props.available / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.available / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Frei </td>
                <td> {{ round(props.free / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.free / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Aktiv </td>
                <td> {{ round(props.active / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.active / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Inaktiv </td>
                <td> {{ round(props.inactive / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.inactive / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Buffers </td>
                <td> {{ round(props.buffers / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.buffers / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Cached </td>
                <td> {{ round(props.cached / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.cached / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Shared </td>
                <td> {{ round(props.shared / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.shared / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Slab </td>
                <td> {{ round(props.slab / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.slab / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
            <tr>
                <td> Wired </td>
                <td> {{ round(props.wired / 1024 / 1024, 3) }} MB</td>
                <td> {{ round(props.wired / 1024 / 1024 / 1024, 3) }} GB</td>
            </tr>
        </tbody>
    </table>
</template>