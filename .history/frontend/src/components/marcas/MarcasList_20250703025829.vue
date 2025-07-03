<template>
  <div>
    <h2>Listado de Marcas</h2>

    <button style="margin-bottom: 1em;">
      <router-link 
        :to="{ name: 'test_create' }" 
        style="text-decoration: none; color: white;"
      >
        Crear Marca (Test)
      </router-link>
    </button>

    <ul>
      <li v-for="marca in store.marcas" :key="marca.id">
        {{ marca.nombre }}
        <router-link
          v-if="marca.id"
          :to="{ name: 'marcas_editar', params: { id: marca.id } }"
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

