<template>
        <router-view/>      
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue';
import  {useRouter, useRoute} from 'vue-router';

const router = useRouter()
const route = useRoute()

// onMounted(()=> {
//         router.push({name:'marcas_list'})
// }) saque la funcion y fue reemplazada en marcas_rutes como redireccionamiento 

</script>

<style scoped>

</style>