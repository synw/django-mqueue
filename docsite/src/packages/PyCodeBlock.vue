<template>
  <div class="pycode-block">
    <div class="code-editor">
      <code-editor :code="parsedCode" @keyup.ctrl.enter="runTheCode()" lang="python" @edit="updateCode($event)"
        :hljs="hljs"></code-editor>
    </div>
    <div v-if="controls == true">
      <button class="code-exec-btn btn neuro" :class="(canRun && !isExecuting) ? 'cursor-pointer' : 'cursor-wait'"
        @click="runTheCode()">
        <template v-if="!canRun">
          <app-icon name="play" class="app-icon icon-lighter"></app-icon>
        </template>
        <template v-else>
          <template v-if="!isExecuting">
            <app-icon name="play" class="app-icon icon-success"></app-icon>
          </template>
          <template v-else>
            <template v-if="log.id == id">
              <app-icon name="python" class="app-icon icon-danger"></app-icon>
            </template>
            <template v-else>
              <app-icon name="play" class="app-icon icon-lighter"></app-icon>
            </template>
          </template>
        </template>
        &nbsp;Execute
      </button>
      <!-- button class="ml-2 cursor-pointer neuro btn" v-if="namespace && controlsClear" @click="clear()">Clear</button -->
    </div>
    <div class="code-output" :class="bottomMargin">
      <div v-if="stdout == true && log.stdOut.length > 0">
        <pre v-for="row in log.stdOut" v-html="row"></pre>
      </div>
      <div v-if="stderr == true && log.stdErr.length > 0">
        <pre v-for="row in log.stdErr" v-html="row"></pre>
      </div>
      <div v-if="exception == true && log.exception">
        <pre v-html="log.exception"></pre>
      </div>
      <div v-if="output == true && outputHtml" v-html="outputHtml"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import "highlight.js";
import { computed, onBeforeUnmount, reactive, ref, Ref, watchEffect } from "vue";
import { usePython } from "usepython";
import { useStore } from '@nanostores/vue';
import { CodeEditor } from "vuecodit";
import AppIcon from "./AppIcon.vue"
import "vuecodit/style.css";
import hljs from 'highlight.js/lib/core';
import python from 'highlight.js/lib/languages/python';
hljs.registerLanguage('python', python);

const props = defineProps({
  id: {
    type: String,
    required: true
  },
  py: {
    type: Object as typeof usePython,
    required: true
  },
  code: {
    type: String,
    required: true,
  },
  namespace: {
    type: String,
    default: null,
  },
  controls: {
    type: Boolean,
    default: true,
  },
  /*controlsClear: {
    type: Boolean,
    default: false,
  },*/
  output: {
    type: Boolean,
    default: true,
  },
  exception: {
    type: Boolean,
    default: true,
  },
  stdout: {
    type: Boolean,
    default: true,
  },
  stderr: {
    type: Boolean,
    default: true,
  },
  dispatch: {
    type: Function
  },
});

const emit = defineEmits(["result"]);

const parsedCode = ref("");
const outputHtml = ref<string | null>(null);
const isReady = useStore(props.py.isReady);
const log = reactive({
  id: "",
  stdOut: new Array<string>(),
  stdErr: new Array<string>(),
  exception: ""
});
const isExecuting: Readonly<Ref<boolean>> = useStore(props.py.isExecuting);

function updateCode(code: string) {
  parsedCode.value = code;
}

async function runTheCode() {
  outputHtml.value = "";
  if (!canRun) {
    return
  }
  const { results, error } = await props.py.run(parsedCode.value, props.namespace, props.id);
  console.log("RR", typeof results, `${results}`);
  if (results) {
    //console.log("RES TYPE", typeof results, results);
    let res = "";
    console.log("TT", typeof res);
    if (results instanceof Map) {
      res = JSON.stringify(Object.fromEntries(results.entries()), null, "  ")
    } else {
      res = `${results}`
    }
    if (props.dispatch) {
      const _res = await props.dispatch(res);
      if (_res != null) {
        res = _res
      } else {
        res = ""
      }
    }
    outputHtml.value = res
    emit("result", outputHtml.value)
  }
};

function clear() {
  props.py.clear(props.namespace);
  outputHtml.value = "";
}

const canRun = computed<Boolean>(() => {
  //return isReady.value == true && isExecuting.value == false
  return isReady.value == true
});

const unbindLog = props.py.log.listen((val) => {
  if (val.id == props.id) {
    log.id = val.id;
    log.stdOut = val.stdOut;
    log.stdErr = val.stdErr;
    log.exception = val.exception;
  }
});

const bottomMargin = computed<string>(() => {
  let m = "";
  if (outputHtml || (outputHtml || log.stdOut.length > 0 || log.stdErr.length > 0)) {
    m = "filled"
  }
  return m
})

onBeforeUnmount(() => unbindLog())
watchEffect(() => {
  parsedCode.value = props.code
  outputHtml.value = "";
})
</script>
