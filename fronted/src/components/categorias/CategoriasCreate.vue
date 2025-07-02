<template>
    <div>
        
    
    <form @submit.prevent="crear">
        <label for="">Nombre de la categoria:</label>
        <input type="text" name="" v-model="categoria.nombre">
        <button>Crear</button>
    </form>

    <button class="btn-volver"><router-link :to="{ name : 'categorias_list'}">Volver</router-link></button>
    </div>
</template>

<script setup lang="ts">
import { ref, toRefs} from 'vue'
import  useCategoriasStore  from '../../stores/categorias'


const { categoria } = toRefs(useCategoriasStore())
const {create} = useCategoriasStore()
//const nombre = ref('')

const crear = async () => {
    if(!categoria.value.nombre) {
        alert('por favor complete el campo')
    } else {
       const response = await create(categoria.value)
       categoria.value.nombre = ''
       alert('La marca fue creada con exito')
    }
}
</script>

<style scoped>

</style>