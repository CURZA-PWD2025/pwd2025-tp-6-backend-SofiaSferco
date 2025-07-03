const marcas_routes = [
  {
    path: '/marcas',
    name: 'marcas',
    component: () => import('../views/MarcasView.vue'),
    redirect: { name: 'marcas_list' },
    children: [
      {
        path: '',
        name: 'marcas_list',
        component: () => import('../components/marcas/MarcasList.vue'),
      },
      {
        path: ':id/show',
        name: 'marcas_detalle',
        component: () => import('../components/marcas/MarcasShow.vue'),
        props: true,
      },
      {
        path: 'crear',
        name: 'marcas_crear',
        component: () => import('../components/marcas/MarcasCreate.vue'),
      },
      {
        path: ':id/editar',
        name: 'marcas_editar',
        component: () => import('../components/marcas/MarcasUpdate.vue'),
        props: true,
      },
    ],
  },
];

export default marcas_routes;
