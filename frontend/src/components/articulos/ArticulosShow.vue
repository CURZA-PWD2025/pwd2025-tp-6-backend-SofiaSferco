<template>
    <div class="container">
        <div class="card">
            <h3>Detalle del articulo:</h3>    
            <h3> nombre: {{  articulo.descripcion }}</h3>
            <h5> id: {{ articulo.id }}</h5>
            <h5> precio: {{ articulo.precio }}</h5>
            <h5> stock: {{ articulo.stock }}</h5>
            <h5> marca: {{ articulo.marca.nombre }}</h5>
            <h5> proveedor: {{ articulo.proveedor.nombre }}</h5>
            <h5>Categorias: 
            <ul>
                <li v-for="cat in articulo.categoria" :key="cat.id">{{ cat.nombre }}</li>
            </ul>
            </h5>
        
        </div>
    </div>
    <button class="btn-volver"><router-link :to="{ name : 'articulos_list'}">Volver</router-link></button>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useMarcaStore from '../../stores/articulos'
import { useRoute } from 'vue-router';

const route = useRoute()
const { articulo, articulos } = toRefs(useMarcaStore())



onMounted (()=> {
    //const id = route.params.id
    //console.log(id)
    //marca.value = marcas.value.find((marca)=> marca.id == parseInt(id))
    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = articulos.value.find((articulo) => articulo.id === parseInt(id));

    if (encontrada) {
    articulo.value = encontrada;
    } else {
    console.warn("Marca no encontrada con id:", id);
    // Podés redirigir, mostrar mensaje, etc.
}

})

</script>
