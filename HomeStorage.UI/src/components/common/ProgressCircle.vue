<script lang="ts" setup>
import { computed } from 'vue';

/** Component Parameters*/
const props = defineProps({
    /** displayed progress percentage  */
    percent: {
        type: Number,
        default: 0
    },

    /** changes wether the percentage text is displayed.  */
    showText: {
        type: Boolean,
        default: true
    },

    /** color of the progress circle.  */
    progressColor: {
        type: String,
        default: "#42b983"
    },

    /** color of the background circle.  */
    backcolor: {
        type: String,
        default: "#ddd"
    },

    /** color of the text.  */
    textcolor: {
        type: String,
        default: "#ddd"
    },
});

const radius = 45
const circumference = 2 * Math.PI * radius
const offset = computed(() => circumference - (props.percent / 100) * circumference)

</script>

<template>
    <div class="progress-circle">
        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle :r="radius" cx="50" cy="50" fill="none" :stroke="props.backcolor" stroke-width="8" />
            <circle :r="radius" cx="50" cy="50" fill="none" :stroke="props.progressColor" stroke-width="10"
                :stroke-dasharray="circumference" :stroke-dashoffset="offset" stroke-linecap="round"
                style="transition: stroke-dashoffset 0.5s" transform="rotate(-90, 50, 50)"/>
            <text x="50" y="57.5" text-anchor="middle" font-size="20" :fill="props.textcolor" >
                {{ props.percent }}%
            </text>
        </svg>
    </div>
</template>

<style scoped>
.progress-circle {
    width: 100%;
    height: 100%;
}

.progress-circle svg {
    width: 100%;
    height: 100%;
}
</style>