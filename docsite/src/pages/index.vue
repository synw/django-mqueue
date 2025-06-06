<template>
  <div class="prosed">
    <h1>{{ libTitle }}</h1>
    <auto-nav v-if="isNavReady" :nodes="nav.tree?.children ?? []" class="space-y-1" :on-open="$router.push"></auto-nav>
  </div>
</template>

<script setup lang="ts">
import { nav, isNavReady } from "@/state";
import { libTitle } from "@/conf";
import { AutoNav } from "@docdundee/vue";
</script>