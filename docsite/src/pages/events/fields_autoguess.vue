<template>
  <div class="prosed">
    <h1>Fields autoguess</h1>
    <p>If you provided an instance or a content_type and a model mqueue will guess the following fields unless you
      provided arguments for:</p>
    <ul>
      <li><kbd>content_type</kbd> <span class="var">ContentType</span> the content type of the associated object</li>
      <li><kbd>obj_pk</kbd> <span class="var">int</span> the primary key of the object</li>
      <li><kbd>admin_url</kbd> <span class="var">str</span> will be reversed from the instance</li>
      <li><kbd>user</kbd> <span class="var">User</span> checks if you model has a <i>user</i> field or an <i>editor</i>
        field and populates from it</li>
      <li><kbd>url</kbd> <span class="var">str</span> checks for a <i>get_event_object_url()</i> method in your model, and
        then check for a <i>get_absolute_url()</i> method and
        populates from it. Write your own <i>get_event_object_url()</i> method in your model to manage which url will be
        associated to the object.</li>
    </ul>
    <h3>Example</h3>
    <p class="not-prose">
      <py-code-block id="1" :code="autoguess" :py="py" namespace="codeblock" class="w-limited"></py-code-block>
    </p>
    <h2>Model fields</h2>
    <p>The <kbd>user</kbd> event property can use custom model field to
      guess it's values. If the model has a <i>user</i> or <i>editor</i> field it will be used to fill
      the <kbd>user</kbd> for the event if not provided as event parameter</p>
    <p>The <kbd>url</kbd> event property can use a custom <i>get_event_object_url()</i> or
      <i>get_absolute_url()</i> model method to
      guess it's values
    </p>
    <static-code-block :hljs="hljs" :code="models" lang="python" class="not-prose"></static-code-block>
  </div>
</template>

<script setup lang="ts">
import { py } from "@/state";
import { hljs } from "@/conf";
import { PyCodeBlock } from "vuepython";
import { StaticCodeBlock } from "@docdundee/vue";
import autoguess from '@/assets/py/events/fields_autoguess.py?raw'
import models from '@/assets/py/events/models.py?raw'
</script>