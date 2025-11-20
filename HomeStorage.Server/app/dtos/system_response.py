from pydantic import BaseModel


class CpuStatsResponse(BaseModel):
    """ 
    Detailed CPU statistics based on psutil. 
    """

    ctx_switches: int = 0
    """
    Number of context switches performed by the system.
    """

    interrupts: int = 0
    """
    Number of hardware interrupts.
    """

    soft_interrupts: int = 0
    """
    Number of software interrupts.
    """

    syscalls: int = 0
    """
    Number of system calls invoked.
    """


class CpuTimesResponse(BaseModel):
    """ 
    Distribution of CPU time across various operating modes. 
    """

    user: float = 0.0
    """
    Time spent in user mode.
    """

    nice: float = 0.0
    """
    Time spent in user mode with a lower (nice) priority.
    """

    system: float = 0.0
    """
    Time spent in kernel mode.
    """

    idle: float = 0.0
    """
    Time during which the CPU was idle.
    """

    iowait: float = 0.0
    """
    Time spent waiting for I/O operations to complete.
    """

    irq: float = 0.0
    """
    Time spent handling hardware interrupts.
    """

    softirq: float = 0.0
    """
    Time spent handling software interrupts.
    """

    steal: float = 0.0
    """
    CPU time stolen by the hypervisor for other virtual machines.
    """

    guest: float = 0.0
    """
    Time spent executing guest virtual machines.
    """

    guest_nice: float = 0.0
    """
    Nice time spent executing guest virtual machines.
    """

    interrupt: float = 0.0
    """
    Time spent for servicing hardware interrupts 
    """

    dpc: float = 0.0
    """
    Time spent servicing deferred procedure calls (DPCs); DPCs are interrupts that run at a lower priority than standard interrupts
    """


class CpuFreqResponse(BaseModel):
    """ 
    CPU frequency information in MHz.
    """

    current: float = 0.0
    """
    Current CPU frequency in MHz.
    """

    min: float = 0.0
    """
    Minimum supported CPU frequency in MHz.
    """

    max: float = 0.0
    """
    Maximum supported CPU frequency in MHz.
    """


class CpuLoadResponse(BaseModel):
    """ 
    Average system load over different time intervals.
    """

    min_1_load: float = 0.0
    """
    Average system load over the last 1 minute.
    """

    min_5_load: float = 0.0
    """
    Average system load over the last 5 minutes.
    """

    min_15_load: float = 0.0
    """
    Average system load over the last 15 minutes.
    """


class SystemCpuResponse(BaseModel):
    """ 
    Aggregated CPU information of the system.
    """

    cpu_count: int = 0
    """
    Number of logical CPU cores.
    """

    cpu_stats: CpuStatsResponse = CpuStatsResponse()
    """
    Basic CPU statistics.
    """

    cpu_load: CpuLoadResponse = CpuLoadResponse()
    """
    Average system load.
    """

    cpu_percs: list[float] = []
    """
    CPU usage per core in percent.
    """

    cpu_times: list[CpuTimesResponse] = []
    """
    CPU time statistics for each individual core.
    """

    cpu_freqs: list[CpuFreqResponse] = []
    """
    CPU frequency information for each core.
    """


class MemoryVirtualResponse(BaseModel):
    """ 
    Detailed information about the virtual memory (RAM).
    """

    total: int = 0
    """
    Total physical memory in bytes.
    """

    available: int = 0
    """
    Immediately available memory without using swap.
    """

    percent: int = 0
    """
    Memory usage in percent.
    """

    used: int = 0
    """
    Used memory, calculated differently depending on the platform.
    """

    free: int = 0
    """
    Unused (zeroed) memory immediately available to the system.
    """

    active: int = 0
    """
    Memory actively used by processes.
    """

    inactive: int = 0
    """
    Memory marked as inactive.
    """

    buffers: int = 0
    """
    Memory used for buffer caches, e.g., filesystem metadata.
    """

    cached: int = 0
    """
    Cached memory segments.
    """

    shared: int = 0
    """
    Memory shared between processes.
    """

    slab: int = 0
    """
    Memory used for in-kernel data structures.
    """

    wired: int = 0
    """
    Memory locked in RAM and not pageable.
    """


class MemorySwapResponse(BaseModel):
    """ 
    Information about swap memory usage.
    """

    total: int = 0
    """
    Total swap memory in bytes.
    """

    used: int = 0
    """
    Used swap memory in bytes.
    """

    free: int = 0
    """
    Free swap memory in bytes.
    """

    percent: int = 0
    """
    Swap usage in percent.
    """

    sin: int = 0
    """
    Total bytes swapped in (cumulative).
    """

    sout: int = 0
    """
    Total bytes swapped out (cumulative).
    """


class SystemMemoryResponse(BaseModel):
    """ 
    Complete memory status of the system.
    """

    virtual: MemoryVirtualResponse = MemoryVirtualResponse()
    """
    Virtual memory information.
    """

    swap: MemorySwapResponse = MemorySwapResponse()
    """
    Swap memory information.
    """


class DiskPartitionResponse(BaseModel):
    """ 
    Description of a single disk partition.
    """

    device: str = ""
    """
    Device path of the partition (e.g., '/dev/sda1').
    """

    mountpoint: str = ""
    """
    Mount point of the partition.
    """

    fstype: str = ""
    """
    Filesystem type (e.g., ext4, NTFS).
    """

    opts: str = ""
    """
    Mount options of the partition.
    """


class DiskUsageResponse(BaseModel):
    """ 
    Usage statistics of a disk or partition.
    """

    device: str = ""
    """
    Name of the referenced partition.
    """

    total: int = 0
    """
    Total storage capacity in bytes.
    """

    used: int = 0
    """
    Used storage in bytes.
    """

    free: int = 0
    """
    Free storage in bytes.
    """

    percent: int = 0
    """
    Disk usage in percent.
    """


class DiskIoCountersResponse(BaseModel):
    """ 
    Mirrors psutil.disk_io_counters(perdisk=True).
    """

    device: str = ""
    """
    Name of the referenced device.
    """

    read_count: int = 0
    """
    Number of completed read operations.
    """

    write_count: int = 0
    """
    Number of completed write operations.
    """

    read_bytes: int = 0
    """
    Total bytes read.
    """

    write_bytes: int = 0
    """
    Total bytes written.
    """

    read_time: int = 0
    """
    Time spent on read operations (ms).
    """

    write_time: int = 0
    """
    Time spent on write operations (ms).
    """

    busy_time: int = 0
    """
    Time the device was busy (ms).
    """

    read_merged_count: int = 0
    """
    Number of merged read operations.
    """

    write_merged_count: int = 0
    """
    Number of merged write operations.
    """


class SystemDiskResponse(BaseModel):
    """ 
    Complete disk information of the system.
    """

    partitions: list[DiskPartitionResponse] = []
    """
    List of all detected disk partitions.
    """

    usage: list[DiskUsageResponse] = []
    """
    Disk space usage information for all partitions.
    """

    io_counters: list[DiskIoCountersResponse] = []
    """
    I/O statistics for all block devices.
    """


class SystemResponse(BaseModel):
    """ 
    Overall system metrics response.
    """

    cpu: SystemCpuResponse = SystemCpuResponse()
    """
    CPU status of the system.
    """

    memory: SystemMemoryResponse = SystemMemoryResponse()
    """
    Memory status of the system.
    """

    disk: SystemDiskResponse = SystemDiskResponse()
    """
    Disk status of the system.
    """
