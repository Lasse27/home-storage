<script setup lang="ts">
import { ref } from 'vue'

const showDialog = ref(false)
</script>

<template>
    <div v-if="showDialog" class="dialog">
        <div class="">
            <h2 class="">Confirm Action</h2>
            <p>Do you really want to delete this item?</p>
            <div class="">
                <button @click="showDialog = false">Cancel</button>
                <button class="" @click="showDialog = false">Delete</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.dialog {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>