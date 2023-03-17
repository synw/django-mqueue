<template>
  <render-md :hljs="hljs" :source="readme"></render-md>
</template>

<script setup lang="ts">
import { hljs } from '@/conf';
import { RenderMd } from '@docdundee/vue';
import readme from "@/assets/README.md?raw"
</script>