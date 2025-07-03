<template>
  <div>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input id="nombre" type="text" v-model="nombre" />
      <button>Crear</button>
    </form>

    <button class="btn-volver">
      <router-link :to="{ name: 'marcas_list' }">Volver</router-link>
    </button>
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
    alert('La marca fue creada con éxito')
    nombre.value = ''
    router.push({ name: 'marcas_list' }) // redirigir al listado luego de crear
  } catch (error) {
    alert('Error al crear la marca. Intente nuevamente.')
    console.error(error)
  }
}
</script>

<style scoped>

</style>

