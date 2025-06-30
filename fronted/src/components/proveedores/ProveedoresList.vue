<template>
  <button class="boton-crear"><router-link :to="{ name: 'proveedores_create' }">Crear Proveedor</router-link></button>

  <table>
    <thead>
      <tr>
        <th>id</th>
        <th>nombre</th>
        <th>telefono</th>
        <th>direccion</th>
        <th>email</th>
        <th>acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="proveedor in proveedores" :key="proveedor.id">
        <td>{{ proveedor.id }}</td>
        <td>{{ proveedor.nombre }}</td>
        <td>{{ proveedor.telefono }}</td>
        <td>{{ proveedor.direccion }}</td>
        <td>{{ proveedor.email }}</td>
        <td>
          <button><router-link :to="{name:'proveedores_edit', params:{id:proveedor.id}}"><Icon icon="tabler:edit" /></router-link></button>
          <button><router-link :to="{name:'proveedores_show', params:{id:proveedor.id}}"><Icon icon="tabler:eye-share" /></router-link></button>
          <button @click.prevent="eliminar(proveedor.id as number)"><Icon icon="tabler:circle-letter-x" /></button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
import { onMounted, toRefs, watch } from 'vue'
import useProveedoresStore from '../../stores/proveedores'
import { Icon } from '@iconify/vue'

const { proveedores } = toRefs(useProveedoresStore())
const { getAll, destroy } = useProveedoresStore()



onMounted(async () => {
  await getAll()
})

async function eliminar(id: number) {
  if (confirm('desea elimina rel registro ' +id+'?')){
    await destroy(id)
  }
  await getAll()
}



</script>

<style scoped>
</style>