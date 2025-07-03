<template>
  <div>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input id="nombre" type="text" v-model="nuevoNombre" />
      <button type="submit">Crear</button>
    </form>

    <button class="btn-volver">
      <router-link :to="{ name: 'marcas_list' }">Volver</router-link>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useMarcasStore } from '../../stores/marcas'

const store = useMarcasStore()
const nuevoNombre = ref('')

const crear = async () => {
  if (!nuevoNombre.value.trim()) {
    alert('Por favor complete el campo')
    return
  }

  await store.create({ id: 0, nombre: nuevoNombre.value.trim() }) // id=0 o null porque lo asigna el backend
  nuevoNombre.value = ''
  alert('La marca fue creada con éxito')
}
</script>
