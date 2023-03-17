<template>
  <the-header :lib-title="libTitle" :links="links"></the-header>
  <div class="p-5 pb-16 mt-16 md:ml-64">
    <router-view></router-view>
  </div>
  <the-sidebar class="fixed left-0 hidden w-64 h-screen p-3 top-16 sm:block secondary"></the-sidebar>
</template>

<script setup lang="ts">
import { onBeforeMount } from "vue";
import TheHeader from "./components/TheHeader.vue";
import TheSidebar from "./components/TheSidebar.vue";
import { libTitle, links } from "@/conf";
import { initState } from "./state";
import { useRouter } from "vue-router";

const router = useRouter();

function openLink(url: string) {
  router.push(url)
}

// global helper for markdown links
// use these links format in markdown files:
// <a href="javascript:openLink('/category/name')">My link</a>
window["openLink"] = openLink;

onBeforeMount(() => initState());
</script>

<style lang="sass">
.var
  color: #b75501
</style>

