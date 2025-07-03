import { createRouter, createWebHistory } from 'vue-router'

import MarcasList from '@/components/marcas/MarcasList.vue'
import CrearMarca from '@/components/marcas/MarcasCreate.vue'
import MarcaDetalle from '@/components/marcas/MarcasShow.vue'
import EditarMarca from '@/components/marcas/MarcasUpdate.vue'
import TestCreate from '@/components/marcas/TestCreate.vue'
const routes = [



const routes = [
  // ...tus rutas
  {
    path: '/test-create',
    name: 'test_create',
    component: TestCreate
  }
]

  {
    path: '/',
    name: 'home',
    redirect: { name: 'marcas_list' }  // redirige al listado de marcas
  },
  {
    path: '/marcas',
    name: 'marcas_list',
    component: MarcasList
  },
  {
    path: '/marcas/crear',
    name: 'marcas_crear',
    component: CrearMarca
  },
  {
    path: '/marcas/:id',
    name: 'marcas_detalle',
    component: MarcaDetalle,
    props: true
  },
  {
    path: '/marcas/:id/editar',
    name: 'marcas_editar',
    component: EditarMarca,
    props: true
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})



export default router
