<template>
  <div>
    <h2>Listado de Marcas</h2>
    <ul>
      <li v-for="marca in store.marcas" :key="marca.id" style="margin-bottom: 0.5em;">
        {{ marca.nombre }}

        <span v-if="marca.id">
          <router-link
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
        </span>

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
  if (confirm('¿Estás seguro de eliminar esta marca?')) {
    store.destroy(id)
  }
}
</script>
