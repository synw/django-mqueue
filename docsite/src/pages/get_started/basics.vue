<template>
  <div class="prosed">
    <h1>Get started</h1>
    <h2>Minimal event</h2>
    <p class="not-prose">
      <py-code-block id="1" :code="code" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
    <h2>Query events</h2>
    <p class="not-prose">
      <py-code-block id="2" :code="qs" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
    <h2>Query by date</h2>
    <p class="not-prose">
      <py-code-block id="3" :code="date" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
  </div>
</template>

<script setup lang="ts">
import { py } from "@/state";
//import { PyCodeBlock } from "vuepython";
import PyCodeBlock from "@/packages/PyCodeBlock.vue";
import qs from '@/assets/py/get_started/qs.py?raw'
import date from '@/assets/py/get_started/date.py?raw'

const code = `from mqueue.models import MEvent
from django.forms.models import model_to_dict

event = MEvent.objects.create(name = 'Something happened!')
model_to_dict(event)`
</script>