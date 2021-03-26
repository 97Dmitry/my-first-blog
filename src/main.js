import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

const app = createApp(App);

// MODULES
app.use(router);
app.use(store);

// MIXINS
// app.mixin(parseDate)




//
app.mount('.app');