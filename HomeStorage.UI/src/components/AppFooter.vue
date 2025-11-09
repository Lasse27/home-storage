<script lang="ts" setup>

</script>

<template>
    <div class="app-footer">
         <div class="footer-body">
            <p>2024 HomeStorage</p>
            <p>v.1.0.0</p>
            <p>118 GB frei von 256 GB</p>
         </div>
    </div>
</template>

<style scoped>
.app-footer {
    background-color: var(--surface);
    padding: 0.25rem;
    text-align: center;
    box-shadow: var(--shadow-sm);
    display: flex;
    justify-content: center;
    border-top: 1px solid var(--border);
}
.footer-body {
    display: flex;
    gap: 2rem;
    font-size: 0.75rem;
}
</style>