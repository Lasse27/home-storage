import axios from "axios";

const apiBase = axios.create({
    baseURL: '/api',
    timeout: 10000, // ms
    headers: { 'Content-Type': 'application/json' }
})

export default apiBase;