import { defineStore } from "pinia";
import { ref } from 'vue';
import type  Marca  from '../interfaces/Proveedores';
import ApiService from "@/services/ApiService";
import type Proveedor from "../interfaces/Proveedores";

const useProveedoresStore =defineStore('proveedores', ()=>{
    const proveedores=ref<Array<Proveedor>>([])
    const proveedor =ref<Proveedor>({
        id:0,
        nombre: '',
        telefono: 0,
        direccion: '',
        email: '',

    })
    const url = 'proveedores'

    // function findMarca(id:number) {
    //     const find_marca=marca.value.find((m) => {
    //         return m.id == id
    //     })
    //     if (find_marca) {
    //         marca.value = find_marca
    //     }
    // }

    //-----------------------------


    // async function getAll() {
    //     const data = await ApiService.getAll(url)
    //     if (data) {
    //         marcas.value = data
    //     }
    //     else {
    //         data.error
    //     }
    // }

    async function getAll() {
        try {
            const data = await ApiService.getAll('proveedores')
            if (data) {
                proveedores.value = data // Actualizo la lista reactiva con lo que devuelve el GET
        }
        } catch (error) {
            console.error('Error al cargar proveedores:', error)
  }
}

    async function getOne(id: number) {
        const data = await ApiService.getOne(url, id)
        if (data) {
            proveedores.value = data
        }
        
    }
    async function create(proveedor: Proveedor) {
    await ApiService.create(url, proveedor)
    const nuevosProveedores = await ApiService.getAll(url)
    proveedores.value = nuevosProveedores
    }

    async function update(proveedor: Proveedor) {
    if(proveedor.id) {
    await ApiService.update('proveedores/',proveedor.id, proveedor)
    }
    }
    // async function destroy(id: number) {
    //     const data = await ApiService.destroy('marcas/', id)
    //     if (data) {
    //         marcas.value = data
    //     }
        
    // }

    async function destroy(id: number) {
    try {
        await ApiService.destroy('proveedores/', id)
        // No actualizar marcas.value aquí
    } catch (error) {
        console.error('Error al eliminar proveedor:', error)
    throw error
    }
}




    return {proveedores, proveedor, getAll, getOne, create, destroy, update}
})

export default useProveedoresStore