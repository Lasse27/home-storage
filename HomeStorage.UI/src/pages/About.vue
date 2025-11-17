<script lang="ts" setup>
import PageHeader from '@/components/PageHeader.vue';
import { Info, } from 'lucide-vue-next'
import MarkdownIt from 'markdown-it';

// full options list (defaults)
const md = MarkdownIt({
    // Enable HTML tags in source
    html: true,

    // Use '/' to close single tags (<br />).
    xhtmlOut: false,

    // Convert '\n' in paragraphs into <br>
    breaks: true,

    // CSS language prefix for fenced blocks. Can be
    // useful for external highlighters.
    langPrefix: 'language-',

    // Autoconvert URL-like text to links
    linkify: true,

    // Enable some language-neutral replacement + quotes beautification
    typographer: true,

    // Double + single quotes replacement pairs, when typographer enabled,
    // and smartquotes on. Could be either a String or an Array.
    //
    // For example, you can use '«»„“' for Russian, '„“‚‘' for German,
    // and ['«\xA0', '\xA0»', '‹\xA0', '\xA0›'] for French (including nbsp).
    quotes: '“”‘’',

    // Highlighter function. Should return escaped HTML, or '' if the source
    highlight: function (/*str, lang*/) { return ''; }
});


</script>

<template>
    <div class="home-page">
        <PageHeader title="Über" :icon="Info" />

    </div>
</template>

<style scoped>
.home-page {
    height: 100%;
    width: 100%;
    box-sizing: border-box;
}
</style>