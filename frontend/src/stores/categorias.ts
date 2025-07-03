import { defineStore } from "pinia";
import { ref } from 'vue';
import ApiService from "@/services/ApiService";
import type Categoria from "../interfaces/Categorias";

const useCategoriasStore =defineStore('categorias', ()=>{
    const categorias=ref<Array<Categoria>>([])
    const categoria =ref<Categoria>({
        id:0,
        nombre: '',
    })
    const url = 'categorias'

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
            const data = await ApiService.getAll('categorias')
            if (data) {
                categorias.value = data // Actualizo la lista reactiva con lo que devuelve el GET
        }
        } catch (error) {
            console.error('Error al cargar marcas:', error)
  }
}

    async function getOne(id: number) {
        const data = await ApiService.getOne(url, id)
        if (data) {
            categorias.value = data
        }
        
    }
    async function create(categoria: Categoria) {
    await ApiService.create(url, categoria)
    const nuevasMarcas = await ApiService.getAll(url)
    categorias.value = nuevasMarcas
    }

        async function update(categoria: Categoria) {
        if(categoria.id) {
            await ApiService.update('categorias/',categoria.id, categoria)
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
        await ApiService.destroy('categorias/', id)
        // No actualizar marcas.value aquí
    } catch (error) {
        console.error('Error al eliminar la categoria:', error)
    throw error
    }
}




    return {categorias, categoria, getAll, getOne, create, destroy, update}
})

export default useCategoriasStore