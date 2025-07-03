<template>
  <div class="container">
    <div class="card">
      <h3>Detalle de la marca:</h3>    
      <h3>Nombre: {{ marca.nombre }}</h3>
      <h5>ID: {{ marca.id }}</h5>
    </div>
    <button class="btn-volver">
      <router-link :to="{ name: 'marcas_list' }">Volver</router-link>
    </button>
  </div>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import { useRoute } from 'vue-router'
import { useMarcasStore } from '../../stores/marcas'  // import con export nombrado

const route = useRoute()
const store = useMarcasStore()
const { marca, marcas } = toRefs(store)

onMounted(() => {
  const idParam = route.params.id
  const id = Array.isArray(idParam) ? idParam[0] : idParam

  const encontrada = marcas.value.find((m) => m.id === Number(id))

  if (encontrada) {
    marca.value = encontrada
  } else {
    console.warn('Marca no encontrada con id:', id)
    // Podés redirigir, mostrar mensaje o lo que necesites acá
  }
})
</script>
