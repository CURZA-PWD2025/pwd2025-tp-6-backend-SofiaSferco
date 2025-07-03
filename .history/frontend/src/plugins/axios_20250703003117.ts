import  axios  from "axios"

export const instance= axios.create({
    baseURL: "http://localhost:5000/",
    timeout:1000,
})
//1
//se simplifica la url en una variable reutilizable que es llamada por nuestra api
//axios es una libreria que permite realizar los put,get,delete , en este caso es lo 
// que permite crear esta instancia con los datos de la url y el tiempo de espera con el backend
// que si no responde en 1 seg se cancela