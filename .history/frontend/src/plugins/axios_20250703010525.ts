import axios from 'axios';

export const instance = axios.create({
  baseURL: 'http://localhost:5000',  // Cambiá por tu URL base si es distinta
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});
