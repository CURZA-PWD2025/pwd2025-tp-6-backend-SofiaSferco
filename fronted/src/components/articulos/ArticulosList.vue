<template>
  <button class="boton-crear"><router-link :to="{ name: 'articulos_create' }">Crear Articulo</router-link></button>

  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>descripcion</th>
        <th>precio</th>
        <th>stock</th>
        <th>marca</th>
        <th>proveedor</th>
        <th>categorias</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="articulo in articulos" :key="articulo.id">
        <td>{{ articulo.id }}</td>
        <td>{{ articulo.descripcion }}</td>
        <td>{{ articulo.precio }}</td>
        <td>{{ articulo.stock }}</td>
        <td>{{ articulo.marca?.nombre || 'SIN MARCA' }}</td>
        <td>{{ articulo.proveedor?.nombre || 'SIN PROVEEDOR' }}</td>
        <td>          
          <ul>
            <li v-for="cat in articulo.categoria" :key="cat.id">{{ cat.nombre }}</li>
          </ul>
        </td>
        <td>
          <button><router-link :to="{ name: 'articulos_edit', params: { id: articulo.id } }"><Icon icon="tabler:edit" /></router-link></button>
          <button><router-link :to="{name:'articulos_show', params:{id:articulo.id}}"><Icon icon="tabler:eye-share" /></router-link></button>
          <button @click.prevent="eliminar(articulo.id as number)"><Icon icon="tabler:circle-letter-x" /></button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useMarcasStore from '../../stores/articulos'
import { Icon } from '@iconify/vue'


const store= useMarcasStore()
const {articulos, articulo} =toRefs(store)


const { getAll, destroy } = useMarcasStore()



onMounted(async () => {
  await store.getAll()
})

async function eliminar(id: number) {
  if (confirm('¿Desea eliminar el registro ' + id + '?')) {
    await store.destroy(id)
    await store.getAll()
  }
}



</script>
<style scoped>

</style>