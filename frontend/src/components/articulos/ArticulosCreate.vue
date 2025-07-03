<template>
  <div>  
    <form @submit.prevent="crear">

      <label>Descripción del artículo:</label>
      <input type="text"  v-model="descripcion"/>

      <label>Precio:</label>
      <input type="text"  v-model="precio"/>

      <label>Stock:</label>
      <input type="text"  v-model="stock"/>

      <label>Marcas:</label>
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

      <button type="submit">Crear</button>
    </form>

    <button class="btn-volver"><router-link :to="{ name : 'articulos_list' }">Volver</router-link></button>
  </div>
</template>

<script setup lang="ts">
import { onMounted , ref} from 'vue'
import useMarcasStore from '@/stores/marcas'
import useProveedoresStore from '@/stores/proveedores'
import useCategoriasStore from '../../stores/categorias'
import type  ArticuloCreate  from '@/interfaces/ArticulosCreate'
import { useRouter } from 'vue-router'
import useArticulosStore from '../../stores/articulos'


const router = useRouter()

const articulosStore=useArticulosStore()
const marcasStore = useMarcasStore()
const proveedoresStore = useProveedoresStore()
const categoriasStore = useCategoriasStore()


const descripcion = ref('')
const precio = ref('')
const stock = ref('')
const marca_id = ref('')
const proveedor_id = ref('')
const categorias = ref<number[]>([])

const crear = async () => {
  const nuevoArticulo: ArticuloCreate = {
    descripcion: descripcion.value,
    precio: precio.value,
    stock: stock.value,
    marca_id: marca_id.value,
    proveedor_id: proveedor_id.value,
    categorias: categorias.value
 }

  try {
    await articulosStore.create(nuevoArticulo)
    //router.push({ name: 'articulos_list' })
    alert ('El articulo fue creado con exito')
    descripcion.value = ''
    precio.value = ''
    stock.value = ''
    marca_id.value = ''
    proveedor_id.value = ''
    categorias.value = []
  } catch (error) {
    console.error('Error al crear artículo:', error)
  }
}

onMounted(async () => {
  await marcasStore.getAll()
  await proveedoresStore.getAll()
  await categoriasStore.getAll()
})

</script>

<style scoped>

</style>