import instance from '@/plugins/axios';

class ApiService {

    static async getAll(url: string) {
        try {
            const response = await axios.get(url)
            if (response) {
                return response.data
            }
        }
        catch (error) {
            return error
        }
    }
    static async getOne(url:string, id:number) {
        try {
            const response= await axios.get(url + id)
            if (response) {
                return response.data
            }
        } catch (error) {
            return error
        }
    }
    static async create(url: string, data: object) {
        try {
            const response = await axios.post(url,data)
            if (response){
                return response.data
            }
        } catch (error) {
            return error
        }
    }
    static async update(url:string, id: number, data:object) {
        try {
            const response = await axios.put(url+id,data)
            if (response){
                return response.data
            }
        } catch (error) {
            return error
        }
    }
    static async destroy(url:string, id:number) {
                try {
            const response= await axios.delete(url + id)
            if (response) {
                return response.data
            }
        } catch (error) {
            return error
        }
    }
    static async updateArticulo(url: string, id: number, data: object) {
        try {
        //const response = await axios.put(`${url}${id}`, data) 
        const cleanUrl = url.endsWith('/') ? url : url + '/'
        const response2 = await axios.put(`${cleanUrl}${id}`, data)
        if (response2) {
            return response2.data
        }
        }
        catch (error) {
        return error
    }
}
}

export default ApiService
//2
//aqui centraliza las funciones de CRUD, son funcciones estandarizadas
// estas son consumidas por cada componente
//IMPORTANTE_ la estructura con try and catch, 
//con put y post se manipula la data que es el json que se envia al backend
//axios en la api repreesenta la instance creada en axios.ts en plugins
