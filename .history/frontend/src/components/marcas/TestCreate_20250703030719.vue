<template>
  <div>
    <h2>Crear Marca (Test)</h2>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input id="nombre" type="text" v-model="nombre" />
      <button type="submit">Crear</button>
    </form>

    <!-- Botón Volver -->
    <button class="btn-volver" style="margin-top:1em;">
      <router-link :to="{ name: 'marcas_list' }" style="text-decoration:none; color: inherit;">
        Volver
      </router-link>
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMarcasStore } from '@/stores/marcas'

const store = useMarcasStore()
const nombre = ref('')

async function crear() {
  if (!nombre.value.trim()) {
    alert('Por favor complete el campo')
    return
  }
  await store.create({ id: 0, nombre: nombre.value })
  alert('Marca creada con éxito')
  nombre.value = ''
}
</script>


