import { defineStore } from "pinia";
import { ref } from 'vue';
import type  Articulo  from '../interfaces/Articulos';
import ApiService from "@/services/ApiService";
import type ArticuloCreate from '../interfaces/ArticulosCreate'
import type ArticulosUpdate from "@/interfaces/ArticulosUpdate";

const useArticulosStore =defineStore('articulos', ()=>{
    const articulos=ref<Array<Articulo>>([])
    const articulo =ref<Articulo>({
        id: 0,
        descripcion: '',
        precio: '',
        stock: 0,
        marca: { id: 0, nombre: '' },
        proveedor: { id: 0, nombre: '', direccion: '', email: '', telefono: 0 },
        categoria: []
    })
    const url = 'articulos'

    async function getAll() {
        try {
            const data = await ApiService.getAll('articulos')
            if (data) {
                articulos.value = data 
        }
        } catch (error) {
            console.error('Error al cargar el articulo:', error)
        }
    }
    async function getOne(id: number) {
        const data = await ApiService.getOne('articulos/', id)
        if (data) {
            articulos.value = data
        }
        return data
        
    }
    async function create(articulo: ArticuloCreate) {
        await ApiService.create(url, articulo)
        const nuevosArticulos = await ApiService.getAll(url)
        articulos.value = nuevosArticulos
    }
    async function update(articulo: Articulo) {
        if(articulo.id) {
            await ApiService.update('articulos/',articulo.id, articulo)
        }
    }
        async function updateArticulo(articulo: ArticulosUpdate) {
        if(articulo.id) {
            await ApiService.updateArticulo('articulos/',articulo.id, articulo)
        }
        const nuevosArticulos = await ApiService.getAll(url)
        articulos.value = nuevosArticulos
    }

    async function destroy(id: number) {
    try {
        await ApiService.destroy('articulos/', id)
    } catch (error) {
        console.error('Error al eliminar el articulo:', error)
    throw error
        }
    }
    return {articulos, articulo, getAll, getOne, create, destroy, update, updateArticulo}
})

export default useArticulosStore

//3
//