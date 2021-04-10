import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import parseDatePlugin from "@/utils/parseDate.plugin";
import messagePlugin from "@/utils/message.plugin";
import tooltipDirective from "@/directives/tooltip.directive";
// import localization from "@/localization/localization.js";

import "materialize-css/dist/js/materialize.min";

const app = createApp(App);

app.use(router);
app.use(store);
app.use(parseDatePlugin);
app.use(messagePlugin);
app.directive("tooltip", tooltipDirective);
// app.use(localization);
app.mount(".app");
