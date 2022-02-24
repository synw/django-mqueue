"use strict";
const $eventIcons = {
  "default": 'fa fa-flash',
  "important": 'fa fa-exclamation',
  "ok": 'fa fa-thumbs-up',
  "info": 'fa fa-info-circle',
  "debug": 'fa fa-cog',
  "warning": 'fa fa-exclamation',
  "error": 'fa fa-exclamation-triangle',
  "edited": 'fa fa-pencil',
  "created": 'fa fa-plus',
  "deleted": 'fa fa-remove',
}

class MEvent {
  msg;
  cls;
  data;
  model;
  icons;
  clsMsg;

  constructor(m, c, d, md, i, cm) {
    this.msg = m;
    this.cls = c;
    this.data = d;
    this.model = md;
    this.icon = i;
    this.clsMsg = cm;
  }
}

function processEvent(event) {
  let cls = "default";
  let clsMsg = cls;
  let model = null;
  if ("event_class" in event) {
    clsMsg = event.event_class;
    if (event.event_class.endsWith("created")) {
      cls = "created";
      model = event.event_class.split(" ")[0];
    } else if (event.event_class.endsWith("deleted")) {
      cls = "deleted";
      model = event.event_class.split(" ")[0];
    } else if (event.event_class.endsWith("edited")) {
      cls = "edited";
      model = event.event_class.split(" ")[0];
    } else if (event.event_class.startsWith("Log")) {
      cls = event.event_class.split(" ")[1].toLowerCase();
      clsMsg = event.event_class;
    } else {
      cls = event.event_class.toLowerCase();
      clsMsg = event.event_class;
    }
  }
  const evt = new MEvent(event.message, cls, event?.data ?? {}, model, $eventIcons[cls], clsMsg)
  console.log(JSON.stringify(evt, null, "  "))
  return evt
}

function livefeed() {
  Alpine.store('livefeed', {
    verbose: false,
    msgs: [],
    init: function (verbose = true) {
      this.verbose = verbose;
      if (verbose) {
        console.log("Init livefeed");
      }
      $instant.addHandler("$livefeed", (msg) => {
        console.log("NEW EVENT", JSON.stringify(msg, null, "  "));
        this.msgs.push(processEvent(msg));
      });
    },
  });
  return Alpine.store('livefeed');
}