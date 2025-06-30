<template>
    <div class="container">
        <div class="card">
            <h3>Detalle de la categoria:</h3>    
            <h3> nombre: {{  categoria.nombre }}</h3>
            <h5> id: {{ categoria.id }}</h5>    
        </div>
    </div>
    <button class="btn-volver"><router-link :to="{ name : 'categorias_list'}">Volver</router-link></button>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useCategoriasStore from '../../stores/categorias'
import { useRoute } from 'vue-router';

const route = useRoute()
const { categoria, categorias } = toRefs(useCategoriasStore())



onMounted (()=> {
    //const id = route.params.id
    //console.log(id)
    //marca.value = marcas.value.find((marca)=> marca.id == parseInt(id))
    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = categorias.value.find((categoria) => categoria.id === parseInt(id));

    if (encontrada) {
    categoria.value = encontrada;
    } else {
    console.warn("Categoria no encontrada con id:", id);
    // Podés redirigir, mostrar mensaje, etc.
}

})

</script>
