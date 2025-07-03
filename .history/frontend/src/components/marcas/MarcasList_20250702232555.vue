<template>
  <button class="boton-crear">
    <router-link :to="{ name: 'marcas_create' }">Crear Marca</router-link>
  </button>

  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="marca in marcas" :key="marca.id">
        <td>{{ marca.id }}</td>
        <td>{{ marca.nombre }}</td>
        <td>
          <button>
            <router-link :to="{name:'marcas_edit', params:{id:marca.id}}">
              <Icon icon="tabler:edit" />
            </router-link>
          </button>
          <button>
            <router-link :to="{name:'marcas_show', params:{id:marca.id}}">
              <Icon icon="tabler:eye-share" />
            </router-link>
          </button>
          <button @click.prevent="eliminar(marca.id as number)">
            <Icon icon="tabler:circle-letter-x" />
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import useMarcasStore from '../../stores/marcas'
import { Icon } from '@iconify/vue'

// Usa una sola instancia del store
const marcasStore = useMarcasStore()
const { marcas } = toRefs(marcasStore)
const { getAll, destroy } = marcasStore

onMounted(async () => {
  await getAll()
})

async function eliminar(id: number) {
  if (confirm('¿Desea eliminar el registro ' + id + '?')) {
    await destroy(id)
    await getAll()
  }
}
</script>

<style scoped>
/* Puedes agregar estilos aquí */
</style>