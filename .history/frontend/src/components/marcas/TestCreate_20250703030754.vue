<template>
  <div>
    <h2>Test Crear Marca</h2>
    <form @submit.prevent="crear">
      <input v-model="nombre" placeholder="Nombre de la marca" />
      <button type="submit">Crear</button>
    </form>

    <button>
      <router-link :to="{ name: 'marcas_list' }">Volver</router-link>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useMarcasStore } from '@/stores/marcas'

const nombre = ref('')
const store = useMarcasStore()
const router = useRouter()

async function crear() {
  if (!nombre.value.trim()) {
    alert('Por favor ingresa un nombre')
    return
  }
  try {
    await store.create({ id: 0, nombre: nombre.value.trim() }) // id=0 para crear
    alert('Marca creada con éxito')
    nombre.value = ''
    router.push({ name: 'marcas_list' }) // vuelve al listado para ver la nueva marca
  } catch (error) {
    alert('Error al crear marca')
    console.error(error)
  }
}
</script>

<style scoped>
button {
  margin-top: 10px;
  cursor: pointer;
}
</style>

