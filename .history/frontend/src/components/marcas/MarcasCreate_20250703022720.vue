<template>
  <div>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input
        id="nombre"
        type="text"
        v-model="store.marca.nombre"
      />
      <button type="submit">Crear</button>
    </form>

    <router-link :to="{ name: 'marcas_list' }">
      <button class="btn-volver">Volver</button>
    </router-link>
  </div>
</template>

<script setup lang="ts">
import { useMarcasStore } from '../../stores/marcas'

const store = useMarcasStore()

const crear = async () => {
  if (!store.marca.nombre) {
    alert('Por favor complete el campo')
  } else {
    await store.create(store.marca)
    store.marca.nombre = ''
    alert('La marca fue creada con éxito')
  }
}
</script>

<style scoped>

</style>


