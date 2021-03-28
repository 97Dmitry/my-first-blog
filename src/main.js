import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import parseDatePlugin from "@/utils/parseDate.plugin"
import messagePlugin from "@/utils/message.plugin";

import "materialize-css/dist/js/materialize.min";


const app = createApp(App);

// MODULES
app.use(router);
app.use(store);
app.use(parseDatePlugin)
app.use(messagePlugin)
app.add

// MIXINS
// app.mixin(parseDate)




//
app.mount('.app');