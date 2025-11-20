import { defaultCpuTimesResponse, type CpuTimesResponse, type SystemCpuResponse } from "@/types/system";
import apiBase from "./api";
import { round } from "./math_helpers";


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

export function generateAverageCpuTimes(cpu_times?: CpuTimesResponse[]): CpuTimesResponse {
    const avg: CpuTimesResponse = defaultCpuTimesResponse();

    if (!cpu_times || cpu_times.length === 0) {
        return avg;
    }

    for (let i = 0; i < cpu_times.length; i++) {
        const times = cpu_times[i];
        avg.user += times?.user ?? 0;
        avg.nice += times?.nice ?? 0;
        avg.system += times?.system ?? 0;
        avg.idle += times?.idle ?? 0;
        avg.iowait += times?.iowait ?? 0;
        avg.irq += times?.irq ?? 0;
        avg.softirq += times?.softirq ?? 0;
        avg.steal += times?.steal ?? 0;
        avg.guest += times?.guest ?? 0;
        avg.guest_nice += times?.guest_nice ?? 0;
        avg.interrupt += times?.interrupt ?? 0;
        avg.dpc += times?.dpc ?? 0;
    }

    const len = cpu_times.length;
    avg.user = round(avg.user / len, 2);
    avg.nice = round(avg.nice / len, 2);
    avg.system = round(avg.system / len, 2);
    avg.idle = round(avg.idle / len, 2);
    avg.iowait = round(avg.iowait / len, 2);
    avg.irq = round(avg.irq / len, 2);
    avg.softirq = round(avg.softirq / len, 2);
    avg.steal = round(avg.steal / len, 2);
    avg.guest = round(avg.guest / len, 2);
    avg.guest_nice = round(avg.guest_nice / len, 2);
    avg.interrupt = round(avg.interrupt / len, 2);
    avg.dpc = round(avg.dpc / len, 2);

    console.log(avg)
    return avg;
}