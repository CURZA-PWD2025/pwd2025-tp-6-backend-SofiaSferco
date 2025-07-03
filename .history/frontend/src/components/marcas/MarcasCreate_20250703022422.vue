<template>
  <div>
    <h2>Crear nueva Marca</h2>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input id="nombre" type="text" v-model="nombre" />
      <button type="submit">Crear</button>
    </form>

    <router-link :to="{ name: 'marcas_list' }">
      <button class="btn-volver">Volver</button>
    </router-link>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useMarcasStore } from '../../stores/marcas'

const router = useRouter()
const store = useMarcasStore()

const nombre = ref('')

const crear = async () => {
  if (!nombre.value.trim()) {
    alert('Por favor complete el campo')
    return
  }

  try {
    await store.create({ id: 0, nombre: nombre.value.trim() })
    alert('Marca creada con éxito')
    nombre.value = ''
    router.push({ name: 'marcas_list' })
  } catch (error) {
    alert('Error al crear la marca')
    console.error(error)
  }
}
</script>

<style scoped>

</style>


