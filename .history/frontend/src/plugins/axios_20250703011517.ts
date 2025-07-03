// src/plugins/axios.ts
import axios from 'axios';

export const instance = axios.create({
  baseURL: 'http://localhost:5000/api', // Ajustá la URL a tu backend
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});
