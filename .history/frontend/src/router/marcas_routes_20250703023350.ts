// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'

// Vista contenedora para el módulo Marcas
import MarcasView from '@/views/MarcasView.vue'

const routes = [
  {
    path: '/',
    redirect: { name: 'marcas_list' }  // Redirige al listado de marcas
  },
  {
    path: '/marcas',
    name: 'marcas',
    component: MarcasView,
    redirect: { name: 'marcas_list' },
    children: [
      {
        path: '',
        name: 'marcas_list',
        component: () => import('@/components/marcas/MarcasList.vue'),
      },
      {
        path: 'crear',
        name: 'marcas_crear',
        component: () => import('@/components/marcas/MarcasCreate.vue'),
      },
      {
        path: ':id/editar',
        name: 'marcas_editar',
        component: () => import('@/components/marcas/MarcasUpdate.vue'),
        props: true
      },
      {
        path: ':id',
        name: 'marcas_detalle',
        component: () => import('@/components/marcas/MarcasShow.vue'),
        props: true
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
