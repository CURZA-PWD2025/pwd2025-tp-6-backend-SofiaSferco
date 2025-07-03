import type Marca  from './Marca'
import type Proveedor from './Proveedores'
import type Categoria from './Categorias'


export default interface Articulo {
  id: number
  descripcion: string
  precio: number | string
  stock: number
  marca: Marca
  proveedor: Proveedor
  categoria: Categoria[] 
}