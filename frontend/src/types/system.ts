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


export interface MemoryVirtualResponse {
    total: number;
    available: number;
    percent: number;
    used: number;
    free: number;
    active: number;
    inactive: number;
    buffers: number;
    cached: number;
    shared: number;
    slab: number;
    wired: number;
}
export function defaultMemoryVirtualResponse(): MemoryVirtualResponse {
    return {
        total: 0,
        available: 0,
        percent: 0,
        used: 0,
        free: 0,
        active: 0,
        inactive: 0,
        buffers: 0,
        cached: 0,
        shared: 0,
        slab: 0,
        wired: 0,
    }
}


export interface MemorySwapResponse {
    total: number;
    used: number;
    free: number;
    percent: number;
    sin: number;
    sout: number;
}
export function defaultMemorySwapResponse(): MemorySwapResponse {
    return {
        total: 0,
        used: 0,
        free: 0,
        percent: 0,
        sin: 0,
        sout: 0,
    }
}


export interface SystemMemoryResponse {
    virtual: MemoryVirtualResponse;
    swap: MemorySwapResponse;
}
export function defaultSystemMemoryResponse(): SystemMemoryResponse {
    return {
        virtual: defaultMemoryVirtualResponse(),
        swap: defaultMemorySwapResponse()
    }
}


export interface DiskPartitionResponse {
    device: String;
    mountpoint: String;
    fstype: String;
    opts: String;
}
export function defaultDiskPartitionResponse(): DiskPartitionResponse {
    return {
        device: "",
        mountpoint: "",
        fstype: "",
        opts: "",
    }
}


export interface DiskUsageResponse {
    device: String;
    total: number;
    used: number;
    free: number;
    percent: number;
}
export function defaultDiskUsageResponse(): DiskUsageResponse {
    return {
        device: "",
        total: 0,
        used: 0,
        free: 0,
        percent: 0,
    }
}


export interface DiskIoCountersResponse {
    device: String;
    read_count: number;
    write_count: number;
    read_bytes: number;
    write_bytes: number;
    read_time: number;
    write_time: number;
    busy_time: number;
    read_merged_count: number;
    write_merged_count: number;
}
export function defaultDiskIoCountersResponse(): DiskIoCountersResponse {
    return {
        device: "",
        read_count: 0,
        write_count: 0,
        read_bytes: 0,
        write_bytes: 0,
        read_time: 0,
        write_time: 0,
        busy_time: 0,
        read_merged_count: 0,
        write_merged_count: 0,
    }
}


export interface SystemDiskResponse {
    partitions: DiskPartitionResponse[]
    usage: DiskUsageResponse[]
    io_counters: DiskIoCountersResponse[]
}
export function defaultSystemDiskResponse(): SystemDiskResponse {
    return {
        partitions: [],
        usage: [],
        io_counters: []
    }
}