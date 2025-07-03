<template>
    <div>
        <form @submit.prevent="crear">
            <label for="">Nombre de la marca:</label>
            <input type="text" v-model="marca.nombre" />
            <button>Crear</button>
        </form>

        <button class="btn-volver">
          <router-link :to="{ name: 'marcas_list' }">Volver</router-link>
        </button>
    </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue'
import { useMarcasStore } from '../../stores/marcas'  // IMPORTAR con export nombrado

const store = useMarcasStore()
const { marca } = toRefs(store)
const { create } = store

const crear = async () => {
    if (!marca.value.nombre) {
        alert('Por favor complete el campo')
    } else {
       await create(marca.value)
       marca.value.nombre = ''
       alert('La marca fue creada con éxito')
    }
}
</script>

<style scoped>
/* Tu estilo acá */
</style>
