const categorias_routes = [
{
  path: '/categorias',
  name: 'categorias',
  component: () => import('../views/CategoriasView.vue'),
  redirect: { name: 'categorias_list' },
  children: [
    {
      path: '',
      name: 'categorias_list',
      component: () => import('../components/categorias/CategoriasList.vue'),
    },
    {
      path: ':id/show',
      name: 'categorias_show',
      component: () => import('../components/categorias/CategoriasShow.vue'),
    },
    {
      path: 'create',
      name: 'categorias_create',
      component: () => import('../components/categorias/CategoriasCreate.vue'),
    },
    {
      path: ':id/edit',
      name: 'categorias_edit',
      component: () => import('../components/categorias/CategoriasUpdate.vue'),
    },
  ]
}]
export default categorias_routes