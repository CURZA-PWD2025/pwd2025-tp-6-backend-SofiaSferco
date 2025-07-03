import { defineStore } from 'pinia';
import { ref } from 'vue';
import type Marca from '../interfaces/Marca';
import ApiService from '@/services/ApiService';

export const useMarcaStore = defineStore('marcas', () => {
  const marcas = ref<Marca[]>([]);
  const marca = ref<Marca>({
    id: 0,
    nombre: '',
  });
  const url = 'marcas';

  async function getAll() {
    try {
      const data = await ApiService.getAll(url);
      console.log('Datos recibidos:', data);
      marcas.value = data ?? [];
    } catch (error) {
      console.error('Error al cargar marcas:', error);
      marcas.value = [];
    }
  }

  async function getOne(id: number) {
    try {
      const data = await ApiService.get(url, id);
      if (data) {
        marca.value = data;
      }
    } catch (error) {
      console.error('Error al cargar la marca:', error);
    }
  }

  async function create(marcaData: Marca) {
    try {
      await ApiService.create(url, marcaData);
      await getAll(); // refrescar lista después de crear
    } catch (error) {
      console.error('Error al crear marca:', error);
    }
  }

  async function update(marcaData: Marca) {
    try {
      if (marcaData.id) {
        await ApiService.update(url, marcaData.id, marcaData);
        await getAll(); // refrescar lista después de actualizar
      }
    } catch (error) {
      console.error('Error al actualizar marca:', error);
    }
  }

  async function destroy(id: number) {
    try {
      await ApiService.delete(url, id);
      await getAll(); // refrescar lista después de borrar
    } catch (error) {
      console.error('Error al eliminar marca:', error);
    }
  }

  return { marcas, marca, getAll, getOne, create, update, destroy };
});
