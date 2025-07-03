<template>
  <nav>
    <div class="home">
      <router-link :to="{ name: 'home' }">
        <Icon icon="tabler:home" />
      </router-link>
    </div>
    <div class="nav-links">
      <router-link :to="{ name: 'marcas_list' }">Marcas</router-link>
      <!-- <router-link :to="{ name: 'categorias_list' }">Categorias</router-link> -->
       <!-- <router-link :to="{ name: 'proveedores_list' }">Proveedores</router-link>-->
      <router-link :to="{ name: 'articulos_list' }">Articulos</router-link>-->
    </div>
  </nav>

  <main>
    <router-view />
  </main>
</template>

<script setup lang="ts">
import { Icon } from '@iconify/vue';
</script>

<style scoped>
nav {
  position: fixed;        /* La fija en la pantalla */
  top: 0;                 /* Pegada al borde superior */
  left: 0;                /* Pegada al borde izquierdo */
  width: 100%;            /* Todo el ancho del navegador */
  background-color: black;
  padding: 1rem;
  display: grid;
  grid-auto-flow: column;
  gap: 1rem;
  z-index: 1000;          /* Asegura que quede por encima de otros elementos */
  height: 3rem;
}
nav .nav-links {
  display: flex;
  justify-content: space-evenly; /* Empuja los links a la derecha */
  gap: 2rem;               /* Espacio más ajustado entre ellos */
}
nav a {
  color: yellow;         
  text-decoration: none;   
}
nav a:visited {
  color: yellow;          
}
nav a:hover {
  color: rgb(133, 114, 8);            
  text-decoration: none; 
}
main {
  padding-top: 2rem;
}
</style>
