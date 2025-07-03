<template>
    <div>  
        <form @submit.prevent="modificar">
        <label for="">Editar marca:</label>
        <input type="text" name="" v-model="marca.nombre">
        <button>modificar</button>
        </form>
        <button class="btn-volver"><router-link :to="{ name : 'marcas_list'}">Volver</router-link></button>
    </div>
</template>

<script setup lang="ts">
import { onMounted, toRefs } from 'vue';
import useMarcaStore from '../../stores/marcas'
import { useRoute } from 'vue-router';

const route = useRoute()
const { marca, marcas } = toRefs(useMarcaStore())
const { update } = useMarcaStore()


onMounted (()=> {
    const idParam = route.params.id;
    const id = Array.isArray(idParam) ? idParam[0] : idParam;
    const encontrada = marcas.value.find((marca) => marca.id === parseInt(id));

    if (encontrada) {
    marca.value = encontrada;
    } else {
    console.warn("Marca no encontrada con id:", id);    
}
})


const modificar = async () => {
    if (!marca.value.nombre) {
        alert ('por favor complete el campo')
    }
    else {
        const response = await update(marca.value)
        
        alert ('marca actualizada correctamente')
    }
}


</script>

<style scoped>

</style>