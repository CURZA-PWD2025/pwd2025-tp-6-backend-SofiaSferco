import { defineStore } from "pinia";
import { ref } from 'vue';
import type  Marca  from '../interfaces/Marca';
import ApiService from "@/services/ApiService";

const useMarcasStore =defineStore('marcas', ()=>{
    const marcas=ref<Array<Marca>>([])
    const marca =ref<Marca>({
        id:0,
        nombre: '',
    })
    const url = 'marcas'

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
            const data = await ApiService.getAll('marcas')
            if (data) {
                marcas.value = data // Actualizo la lista reactiva con lo que devuelve el GET
        }
        } catch (error) {
            console.error('Error al cargar marcas:', error)
  }
}

    async function getOne(id: number) {
        const data = await ApiService.getOne(url, id)
        if (data) {
            marcas.value = data
        }
        
    }
    async function create(marca: Marca) {
    await ApiService.create(url, marca)
    const nuevasMarcas = await ApiService.getAll(url)
    marcas.value = nuevasMarcas
    }

        async function update(marca: Marca) {
        if(marca.id) {
            await ApiService.update('marcas/',marca.id, marca)
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
        await ApiService.destroy('marcas/', id)
        // No actualizar marcas.value aquí
    } catch (error) {
        console.error('Error al eliminar marca:', error)
    throw error
    }
}




    return {marcas, marca, getAll, getOne, create, destroy, update}
})

export default useMarcasStore