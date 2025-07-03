import { createApp } from 'vue'
import App from './App.vue'
import router from './router'         // Importar router
import { createPinia } from 'pinia'

const app = createApp(App)

app.use(createPinia())
app.use(router)                      // Usar router en la app

app.mount('#app')
