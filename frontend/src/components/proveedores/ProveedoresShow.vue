<template>
    <div class="container">
        <div class="card">
            <h3>Detalle del proveedor:</h3>    
            <h3> nombre: {{  proveedor.nombre }}</h3>
            <h5> id: {{ proveedor.id }}</h5>
            <h5> telefono: {{ proveedor.telefono }}</h5>
            <h5> direccion: {{ proveedor.direccion }}</h5>
            <h5> email: {{ proveedor.email }}</h5>
        </div>
    </div>
    <button class="btn-volver"><router-link :to="{ name : 'proveedores_list'}">Volver</router-link></button>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useProveedoresStore from '../../stores/proveedores'
import { useRoute } from 'vue-router';

const route = useRoute()
const { proveedor, proveedores } = toRefs(useProveedoresStore())



onMounted (()=> {
    //const id = route.params.id
    //console.log(id)
    //marca.value = marcas.value.find((marca)=> marca.id == parseInt(id))
    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = proveedores.value.find((proveedor) => proveedor.id === parseInt(id));

    if (encontrada) {
    proveedor.value = encontrada;
    } else {
    console.warn("Marca no encontrada con id:", id);
    // Podés redirigir, mostrar mensaje, etc.
}

})

</script>
