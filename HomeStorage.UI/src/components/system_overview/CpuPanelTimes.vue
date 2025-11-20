<script setup lang="ts">

const props = defineProps({
    user: Number,
    nice: Number,
    system: Number,
    idle: Number,
    iowait: Number,
    irq: Number,
    softirq: Number,
    steal: Number,
    guest: Number,
    guest_nice: Number,
    interrupt: Number,
    dpc: Number
})

</script>

<template>
    <table>
        <thead>
            <tr>
                <th>Zeiten</th>
                <th>Dauer</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> Nutzermodus</td>
                <td>{{ props.user }} Sekunden</td>
            </tr>
            <tr>
                <td> Nutzermodus (priorisiert)</td>
                <td>{{ props.nice }} Sekunden</td>
            </tr>
            <tr>
                <td> Kernelmodus</td>
                <td>{{ props.system }} Sekunden</td>
            </tr>
            <tr>
                <td> Idle</td>
                <td>{{ props.idle }} Sekunden</td>
            </tr>
            <tr>
                <td> I/O Wartezeit</td>
                <td>{{ props.iowait }} Sekunden</td>
            </tr>
            <tr>
                <td> Hardware-Interrupts (Linux)</td>
                <td>{{ props.irq }} Sekunden</td>
            </tr>
            <tr>
                <td> Software-Interrupts</td>
                <td>{{ props.softirq }} Sekunden</td>
            </tr>
            <tr>
                <td> Virtualisierung</td>
                <td>{{ props.steal }} Sekunden</td>
            </tr>
            <tr>
                <td> Virtual Guest CPU</td>
                <td>{{ props.guest }} Sekunden</td>
            </tr>
            <tr>
                <td> Virtual Guest CPU (priorisiert)</td>
                <td>{{ props.guest_nice }} Sekunden</td>
            </tr>
            <tr>
                <td> Hardware-Interrupts (Windows)</td>
                <td>{{ props.interrupt }} Sekunden</td>
            </tr>
            <tr>
                <td> DPC-Interrupts (Windows)</td>
                <td>{{ props.dpc }} Sekunden</td>
            </tr>
        </tbody>
    </table>
</template>