<template>
    <div>   
        <form @submit.prevent="modificar">
        <label for="">Editar categoria:</label>
        <input type="text" name="" v-model="categoria.nombre">
        <button>modificar</button>
        </form>
        <button class="btn-volver"><router-link :to="{ name : 'categorias_list'}">Volver</router-link></button>
    </div>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useCategoriasStore from '../../stores/categorias'
import { useRoute } from 'vue-router';

const route = useRoute()
const { categoria, categorias } = toRefs(useCategoriasStore())
const { update } = useCategoriasStore()


onMounted (()=> {

    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = categorias.value.find((categoria) => categoria.id === parseInt(id));

    if (encontrada) {
    categoria.value = encontrada;
    } else {
    console.warn("Categoria no encontrada con id:", id);
}

})


const modificar = async () => {
    if (!categoria.value.nombre) {
        alert ('por favor complete el campo')
    }
    else {
        const response = await update(categoria.value)
        
        alert ('Categoria actualizada correctamente')


    }
}


</script>

<style scoped>

</style>