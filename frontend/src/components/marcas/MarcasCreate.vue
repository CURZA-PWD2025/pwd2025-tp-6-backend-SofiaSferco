<template>
    <div>
        
    
    <form @submit.prevent="crear">
        <label for="">Nombre de la marca:</label>
        <input type="text" name="" v-model="marca.nombre">
        <button>Crear</button>
    </form>

    <button class="btn-volver"><router-link :to="{ name : 'marcas_list'}">Volver</router-link></button>
    </div>
</template>

<script setup lang="ts">
import { ref, toRefs} from 'vue'
import  useMarcaStore  from '../../stores/marcas'


const { marca } = toRefs(useMarcaStore())
const {create} = useMarcaStore()
//const nombre = ref('')

const crear = async () => {
    if(!marca.value.nombre) {
        alert('por favor complete el campo')
    } else {
       const response = await create(marca.value)
       marca.value.nombre = ''
       alert('La marca fue creada con exito')
    }
}
</script>

<style scoped>

</style>