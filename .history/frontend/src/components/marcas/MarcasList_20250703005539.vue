<template>
  <div>
    <h2>Listado de Marcas</h2>
    <ul>
      <li v-for="marca in store.marcas" :key="marca.id">
        {{ marca.nombre }}
        <router-link
          v-if="marca.id"
          :to="{ name: 'marcas_edit', params: { id: marca.id } }"
        >Editar</router-link>
        <span v-else>Sin ID</span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useMarcasStore } from '@/stores/marcas'

const store = useMarcasStore()

onMounted(async () => {
  await store.getAll()
})
</script>
