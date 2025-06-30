<template>
    <div>  
        <form @submit.prevent="modificar">
        <label for="">Editar proveedor: </label>
        <input type="text" name="" v-model="proveedor.nombre">
        <label for="">Telefono: </label>
        <input type="text" name="" v-model="proveedor.telefono">
        <label for="">Direccion: </label>
        <input type="text" name="" v-model="proveedor.direccion">
        <label for="">Email: </label>
        <input type="text" name="" v-model="proveedor.email">
        <button>modificar</button>
        </form>
        <button class="btn-volver"><router-link :to="{ name : 'proveedores_list'}">Volver</router-link></button>
    </div>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useProveedoresStore from '../../stores/proveedores'
import { useRoute } from 'vue-router';

const route = useRoute()
const { proveedor, proveedores } = toRefs(useProveedoresStore())
const { update } = useProveedoresStore()


onMounted (()=> {
    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = proveedores.value.find((proveedor) => proveedor.id === parseInt(id));

    if (encontrada) {
    proveedor.value = encontrada;
    } else {
    console.warn("Proveedor no encontrada con id:", id);
}

})


const modificar = async () => {
    if (!proveedor.value.nombre) {
        alert ('por favor complete el campo')
    }
    else {
        const response = await update(proveedor.value)
        
        alert ('proveedor actualizado correctamente')


    }
}


</script>

<style scoped>

</style>