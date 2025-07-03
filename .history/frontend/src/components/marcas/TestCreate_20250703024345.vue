<template>
  <div>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input id="nombre" type="text" v-model="nuevoNombre" />
      <button type="submit">Crear</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const nuevoNombre = ref('')

const crear = () => {
  alert(`Creando marca: ${nuevoNombre.value}`)
  nuevoNombre.value = ''
}
</script>

<style scoped>
button {
  margin-top: 10px;
  padding: 6px 12px;
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
  font-size: 16px;
}

input {
  padding: 4px 8px;
  font-size: 16px;
  margin-top: 6px;
  display: block;
}
</style>
