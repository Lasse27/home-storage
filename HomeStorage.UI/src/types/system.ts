export interface CpuStatsResponse {
    ctx_switches: number;
    interrupts: number;
    soft_interrupts: number;
    syscalls: number;
}


export interface CpuTimesResponse {
    user: number;
    nice: number;
    system: number;
    idle: number;
    iowait: number;
    irq: number;
    softirq: number;
    steal: number;
    guest: number;
    guest_nice: number;
}


export interface CpuFreqResponse {
    current: number;
    min: number;
    max: number;
}


export interface CpuLoadResponse {
    min_1_load: number;
    min_5_load: number;
    min_15_load: number;
}


export interface SystemCpuResponse {
    cpu_count: number;
    cpu_stats: CpuStatsResponse;
    cpu_load: CpuLoadResponse;
    cpu_percs: number[]
    cpu_times: CpuTimesResponse[]
    cpu_freqs: CpuFreqResponse[]
}