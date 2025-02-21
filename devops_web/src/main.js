import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import axios from "./api/http"

const app = createApp(App).use(router)

for (const iconName in ElementPlusIconsVue) {
    app.component(iconName, ElementPlusIconsVue[iconName])
}

app.config.globalProperties.$http=axios
app.use(ElementPlus)
app.mount('#app')
