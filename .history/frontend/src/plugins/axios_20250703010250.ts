import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:5000', // o la URL que uses para tu backend
  timeout: 5000, // 5 segundos, o más si querés
});
