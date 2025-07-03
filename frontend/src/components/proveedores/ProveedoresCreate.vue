<template>
    <div>
        
    
    <form @submit.prevent="crear">
        <label for="">Nombre del proveedor: </label>
        <input type="text" name="" v-model="proveedor.nombre">
        <label for="">Telefono: </label>
        <input type="text" name="" v-model="proveedor.telefono">
        <label for="">Direccion: </label>
        <input type="text" name="" v-model="proveedor.direccion">
        <label for="">Email: </label>
        <input type="text" name="" v-model="proveedor.email">
        <button>Crear</button>
    </form>

    <button class="btn-volver"><router-link :to="{ name : 'proveedores_list'}">Volver</router-link></button>
    </div>
</template>

<script setup lang="ts">
import { ref, toRefs} from 'vue'
import  useProveedoresStore  from '../../stores/proveedores'


const { proveedor } = toRefs(useProveedoresStore())
const {create} = useProveedoresStore()
//const nombre = ref('')

const crear = async () => {
    if(!proveedor.value.nombre && !proveedor.value.telefono && !proveedor.value.direccion && !proveedor.value.email) {
        alert('por favor complete el campo')
    } else {
       const response = await create(proveedor.value)
       proveedor.value.nombre = ''
       alert('El proveedor fue creado con exito')
    }
}
</script>

<style scoped>

</style>