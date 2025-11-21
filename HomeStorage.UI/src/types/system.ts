export interface CpuStatsResponse {
    ctx_switches: number;
    interrupts: number;
    soft_interrupts: number;
    syscalls: number;
}

export function defaultCpuStatsResponse(): CpuStatsResponse {
    return {
        ctx_switches: 0,
        interrupts: 0,
        soft_interrupts: 0,
        syscalls: 0,
    }
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
    interrupt: number;
    dpc: number;
}

export function defaultCpuTimesResponse(): CpuTimesResponse {
    return {
        user: 0,
        nice: 0,
        system: 0,
        idle: 0,
        iowait: 0,
        irq: 0,
        softirq: 0,
        steal: 0,
        guest: 0,
        guest_nice: 0,
        interrupt: 0,
        dpc: 0,
    }
}


export interface CpuFreqResponse {
    current: number;
    min: number;
    max: number;
}

export function defaultCpuFreqResponse(): CpuFreqResponse {
    return {
        current: 0,
        min: 0,
        max: 0,
    }
}


export interface CpuLoadResponse {
    min_1_load: number;
    min_5_load: number;
    min_15_load: number;
}


export function defaultCpuLoadResponse(): CpuLoadResponse {
    return {
        min_1_load: 0,
        min_5_load: 0,
        min_15_load: 0,
    }
}


export interface SystemCpuResponse {
    cpu_count: number;
    cpu_stats: CpuStatsResponse;
    cpu_load: CpuLoadResponse;
    cpu_percs: number[]
    cpu_times: CpuTimesResponse[]
    cpu_freqs: CpuFreqResponse[]
}


export function defaultSystemCpuResponse(): SystemCpuResponse {
    return {
        cpu_count: 0,
        cpu_stats: defaultCpuStatsResponse(),
        cpu_load: defaultCpuLoadResponse(),
        cpu_percs: [],
        cpu_times: [],
        cpu_freqs: []
    }
}