<template>
    <div class="container">
        <div class="card">
            <h3>Detalle de la marca:</h3>    
            <h3> nombre: {{  marca.nombre }}</h3>
            <h5> id: {{ marca.id }}</h5>
        </div>
    </div>
    <button class="btn-volver"><router-link :to="{ name : 'marcas_list'}">Volver</router-link></button>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useMarcaStore from '../../stores/marcas'
import { useRoute } from 'vue-router';

const route = useRoute()
const { marca, marcas } = toRefs(useMarcaStore())



onMounted (()=> {
    //const id = route.params.id
    //console.log(id)
    //marca.value = marcas.value.find((marca)=> marca.id == parseInt(id))
    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = marcas.value.find((marca) => marca.id === parseInt(id));

    if (encontrada) {
    marca.value = encontrada;
    } else {
    console.warn("Marca no encontrada con id:", id);
    // Podés redirigir, mostrar mensaje, etc.
}

})

</script>
