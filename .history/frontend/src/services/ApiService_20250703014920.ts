import { instance } from '@/plugins/axios';

export default {
  async getAll(resource: string) {
    const response = await instance.get(`/${resource}`);
    return response.data;
  },

  async get(resource: string, id: number | string) {
    const response = await instance.get(`/${resource}/${id}`);
    return response.data;
  },

  async create(resource: string, data: any) {
    const response = await instance.post(`/${resource}`, data);
    return response.data;
  },

  async update(resource: string, id: number | string, data: any) {
    const response = await instance.put(`/${resource}/${id}`, data);
    return response.data;
  },

  async delete(resource: string, id: number | string) {
    const response = await instance.delete(`/${resource}/${id}`);
    return response.data;
  }
};
