import type { SystemCpuResponse } from "@/types/system";
import apiBase from "./api";


export async function fetchSystemInfo() {
    const res = await apiBase.get('/system');
    return res.data;
}


export async function fetchCpuInfo(): Promise<SystemCpuResponse> {
    const res = await apiBase.get<SystemCpuResponse>('/system/cpu');
    return res.data;
}


export async function fetchMemoryInfo() {
    const res = await apiBase.get('/system/memory');
    return res.data;
}


export async function fetchDiskInfo() {
    const res = await apiBase.get('/system/disk');
    return res.data;
}