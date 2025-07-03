<template>


  <button class="boton-crear"><router-link :to="{ name: 'categorias_create' }">Crear categoria</router-link></button>

  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="categoria in categorias" :key="categoria.id">
        <td>{{ categoria.id }}</td>
        <td>{{ categoria.nombre }}</td>
        <td>
          <button><router-link :to="{name:'categorias_edit', params:{id:categoria.id}}"><Icon icon="tabler:edit" /></router-link></button>
          <button><router-link :to="{name:'categorias_show', params:{id:categoria.id}}"><Icon icon="tabler:eye-share" /></router-link></button>
          <button @click.prevent="eliminar(categoria.id as number)"><Icon icon="tabler:circle-letter-x" /></button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useCategoriasStore from '../../stores/categorias'
import { Icon } from '@iconify/vue'

const { categorias } = toRefs(useCategoriasStore())
const { getAll, destroy } = useCategoriasStore()



onMounted(async () => {
  await getAll()
})

async function eliminar(id: number) {
  if (confirm('desea elimina rel registro ' +id+'?')){
    await destroy(id)
  }
  await getAll()
}



</script>

<style scoped>
</style>