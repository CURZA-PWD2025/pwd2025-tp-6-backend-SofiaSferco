<template>
        <router-view/>      
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue';
import  {useRouter, useRoute} from 'vue-router';

const router = useRouter()
const route = useRoute()


</script>

<style scoped>

</style>