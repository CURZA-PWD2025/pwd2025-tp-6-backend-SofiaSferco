<template>
  <div>
    <form @submit.prevent="crear">
      <label for="nombre">Nombre de la marca:</label>
      <input
        id="nombre"
        type="text"
        v-model="nombre"
        placeholder="Ingrese nombre de marca"
      />
      <button type="submit">Crear</button>
    </form>

    <button class="btn-volver" @click="volver">
      Volver
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useMarcasStore } from '../../stores/marcas'

const router = useRouter()
const store = useMarcasStore()
const nombre = ref('')  // Campo editable local

const crear = async () => {
  if (!nombre.value.trim()) {
    alert('Por favor complete el campo')
    return
  }

  await store.create({ nombre: nombre.value } as any)
  alert('La marca fue creada con éxito')
  nombre.value = ''
  router.push({ name: 'marcas_list' })
}

const volver = () => {
  router.push({ name: 'marcas_list' })
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  max-width: 300px;
}

input {
  padding: 0.5rem;
}

button {
  margin-top: 1rem;
}
</style>
