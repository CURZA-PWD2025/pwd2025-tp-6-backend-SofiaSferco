import { defineStore } from "pinia";
import { ref } from 'vue';
import type Marca from '../interfaces/Marca';
import ApiService from "@/services/ApiService";

export const useMarcasStore = defineStore('marcas', () => {
    const marcas = ref<Array<Marca>>([]);
    const marca = ref<Marca>({
        id: 0,
        nombre: '',
    });
    const url = 'marcas/';

    async function getAll() {
        try {
            const data = await ApiService.getAll(url);
            if (data) {
                marcas.value = data;
            } else {
                marcas.value = [];
            }
        } catch (error) {
            console.error('Error al cargar marcas:', error);
        }
    }

    async function getOne(id: number) {
        const data = await ApiService.getOne(url, id);
        if (data) {
            marca.value = data;
        }
    }

    async function create(marcaData: Marca) {
        await ApiService.create(url, marcaData);
        const nuevasMarcas = await ApiService.getAll(url);
        marcas.value = nuevasMarcas;
    }

    async function update(marcaData: Marca) {
        if (marcaData.id) {
            await ApiService.update(url, marcaData.id, marcaData);
        }
    }

    async function destroy(id: number) {
        try {
            await ApiService.destroy(url, id);
        } catch (error) {
            console.error('Error al eliminar marca:', error);
            throw error;
        }
    }

    return { marcas, marca, getAll, getOne, create, destroy, update };
});
