<template>
  <div>  
    <form @submit.prevent="modificar">
      <label for="">Editar marca:</label>
      <input type="text" v-model="marca.nombre" />
      <button>Modificar</button>
    </form>
    <button class="btn-volver">
      <router-link :to="{ name: 'marcas_list' }">Volver</router-link>
    </button>
  </div>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue'
import { useRoute } from 'vue-router'
import { useMarcasStore } from '../../stores/marcas'  // Import con export nombrado

const route = useRoute()
const store = useMarcasStore()
const { marca, marcas } = toRefs(store)
const { update } = store

onMounted(() => {
  const idParam = route.params.id
  const id = Array.isArray(idParam) ? idParam[0] : idParam
  const encontrada = marcas.value.find((m) => m.id === Number(id))

  if (encontrada) {
    marca.value = encontrada
  } else {
    console.warn('Marca no encontrada con id:', id)
    // Podés redirigir o mostrar mensaje
  }
})

const modificar = async () => {
  if (!marca.value.nombre) {
    alert('Por favor complete el campo')
    return
  }
  try {
    await update(marca.value)
    alert('Marca actualizada correctamente')
  } catch (error) {
    alert('Error al actualizar la marca')
    console.error(error)
  }
}
</script>

<style scoped>
/* Agregá estilos si querés */
</style>
