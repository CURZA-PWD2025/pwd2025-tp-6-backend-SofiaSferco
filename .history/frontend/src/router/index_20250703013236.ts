import { createRouter, createWebHistory } from 'vue-router'

import MarcasList from '@/components/marcas/MarcasList.vue'
import CrearMarca from '@/components/marcas/CrearMarca.vue'
import MarcaDetalle from '@/components/marcas/MarcaDetalle.vue'
import EditarMarca from '@/components/marcas/EditarMarca.vue'

const routes = [
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
  // Podés agregar aquí más rutas si querés
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
