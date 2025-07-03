<template>
  <div>   
    <form @submit.prevent="modificar">

      <label>Editar artículo:</label>
      <input type="text" v-model="descripcion" />

      <label>Precio:</label>
      <input type="text" v-model="precio" />

      <label>Stock:</label>
      <input type="text" v-model="stock" />

      <label>Marca:</label>
      <select v-model="marca_id">
        <option v-for="m in marcasStore.marcas" :key="m.id" :value="m.id">
          {{ m.nombre }}
        </option>
      </select>

      <label>Proveedor:</label>
      <select v-model="proveedor_id">
        <option v-for="p in proveedoresStore.proveedores" :key="p.id" :value="p.id">
          {{ p.nombre }}
        </option>
      </select>

      <label>Categorías:</label>
      <select multiple v-model="categorias">
        <option v-for="c in categoriasStore.categorias" :key="c.id" :value="c.id">
          {{ c.nombre }}
        </option>
      </select>

      <button type="submit">Actualizar</button>
    </form>

    <button class="btn-volver"><router-link :to="{ name: 'articulos_list' }">Volver</router-link></button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

import useMarcasStore from '@/stores/marcas'
import useProveedoresStore from '@/stores/proveedores'
import useCategoriasStore from '@/stores/categorias'
import useArticulosStore from '@/stores/articulos'

import type ArticuloCreate from '@/interfaces/ArticulosCreate'

const route = useRoute()
const id = ref<number>(Number(route.params.id)) 

const articulosStore = useArticulosStore()
const marcasStore = useMarcasStore()
const proveedoresStore = useProveedoresStore()
const categoriasStore = useCategoriasStore()

const articulo_id = ref<number | null>(null)
const descripcion = ref('')
const precio = ref('')
const stock = ref('')
const marca_id = ref('')
const proveedor_id = ref('')
const categorias = ref<number[]>([])

const modificar = async () => {
  if (articulo_id.value === null) {
    alert('Error: ID del artículo no definido')
    return
  }

  const articuloActualizado: ArticuloCreate & { id: number } = {
    id: articulo_id.value,
    descripcion: descripcion.value,
    precio: precio.value,
    stock: stock.value,
    marca_id: marca_id.value,
    proveedor_id: proveedor_id.value,
    categorias: categorias.value
  }

  try {
    await articulosStore.updateArticulo(articuloActualizado)
    alert('El artículo fue actualizado con éxito')
  } catch (error) {
    console.error('Error al actualizar artículo:', error)
  }
}

onMounted(async () => {
  await marcasStore.getAll()
  await proveedoresStore.getAll()
  await categoriasStore.getAll()

  articulo_id.value = id.value

  const articulo = await articulosStore.getOne(id.value)

  descripcion.value = articulo.descripcion
  precio.value = articulo.precio
  stock.value = articulo.stock
  marca_id.value = articulo.marca_id
  proveedor_id.value = articulo.proveedor_id
  categorias.value = articulo.categorias || []
})
</script>

<style scoped>

</style>