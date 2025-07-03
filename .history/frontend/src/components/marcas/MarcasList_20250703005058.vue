<template>
  <div>
    <h2>Listado de Marcas</h2>
    <ul>
      <li v-for="marca in marcas" :key="marca.id">
        {{ marca.descripcion }}
        
        <router-link :to="{ name: 'marcas_edit', params: { id: marca.id } }">Editar</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMarcasStore } from '@/stores/marcas'

const store = useMarcasStore()
const marcas = ref([])

onMounted(async () => {
  await store.getAll()
  marcas.value = store.marcas
})
</script>
