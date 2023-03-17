<template>
  <div class="prosed">
    <h1>Query events</h1>
    <h2>Events for model</h2>
    <p>List events for a model</p>
    <p class="not-prose">
      <py-code-block id="1" :code="query" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
    <h2>Events for object</h2>
    <p>List events for an object</p>
    <p class="not-prose">
      <py-code-block id="2" :code="query2" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
    <h2>Classic Django queries</h2>
    <p class="not-prose">
      <py-code-block id="3" :code="query3" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
  </div>
</template>

<script setup lang="ts">
import { py } from "@/state";
import { PyCodeBlock } from "vuepython";
import query from '@/assets/py/events/query.py?raw'
import query2 from '@/assets/py/events/query2.py?raw'
import query3 from '@/assets/py/events/query3.py?raw'
</script>