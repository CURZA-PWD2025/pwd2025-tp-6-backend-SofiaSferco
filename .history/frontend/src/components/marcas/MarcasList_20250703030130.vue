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
      <li v-for="marca in store.marcas" :key="marca.id" style="margin-bottom: 0.5em;">
        {{ marca.nombre }}
        
        <router-link
          v-if="marca.id"
          :to="{ name: 'marcas_editar', params: { id: marca.id } }"
          style="margin-left: 1em;"
        >
          Editar
        </router-link>

        <button
          @click="eliminar(marca.id)"
          style="margin-left: 1em; color: red; cursor: pointer; background: none; border: none;"
        >
          Eliminar
        </button>

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

function eliminar(id) {
  if (confirm('¿Querés eliminar esta marca?')) {
    store.destroy(id)
  }
}
</script>
