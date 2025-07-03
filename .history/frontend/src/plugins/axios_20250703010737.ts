import axios from 'axios';

export const instance = axios.create({
  baseURL: 'http://localhost:5000/api',  // Cambiá al URL de tu backend
  timeout: 3000,
  headers: {
    'Content-Type': 'application/json'
  }
});
