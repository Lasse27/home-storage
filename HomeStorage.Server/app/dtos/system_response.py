from pydantic import BaseModel


class CpuStatsResponse(BaseModel):
    """
    Basis-Statistiken der CPU, wie sie von psutil geliefert werden.
    """
    # Anzahl der Kontextwechsel
    ctx_switches: int = 0.0
    # Anzahl der Hardware-Interrupts (Tippfehler!)
    interrups: int = 0.0
    # Anzahl der Software-Interrupts (Tippfehler!)
    soft_interrups: int = 0.0
    # Anzahl der Systemaufrufe
    syscalls: int = 0.0


class CpuTimesResponse(BaseModel):
    """
    Zeitaufteilung der CPU in verschiedene Betriebsmodi.
    """
    # Zeit im User-Mode
    user: float = 0.0
    # Zeit im User-Mode mit Low-Priority (nice)
    nice: float = 0.0
    # Zeit im Kernel-Mode
    system: float = 0.0
    # Leerlaufzeit
    idle: float = 0.0
    # Warten auf I/O
    iowait: float = 0.0
    # Hardware-Interrupt-Verarbeitung
    irq: float = 0.0
    # Software-Interrupt-Verarbeitung
    softirq: float = 0.0
    # Zeit, die der Hypervisor 'gestohlen' hat
    steal: float = 0.0
    # Zeit, die für virtuelle Maschinen genutzt wird
    guest: float = 0.0
    # Nice-Zeit für virtuelle Maschinen
    guest_nice: float = 0.0


class CpuFreqResponse(BaseModel):
    """Informationen zur aktuellen und möglichen CPU-Frequenz."""
    # Aktuelle Taktfrequenz
    current: float = 0.0
    # Minimale mögliche Taktfrequenz
    min: float = 0.0
    # Maximale mögliche Taktfrequenz
    max: float = 0.0


class CpuLoadResponse(BaseModel):
    """Durchschnittliche Systemlast über verschiedene Zeiträume."""
    # Last der letzten 1 Minute
    min_1_load: float = 0.0
    # Last der letzten 5 Minuten
    min_5_load: float = 0.0
    # Last der letzten 15 Minuten
    min_15_load: float = 0.0


class SystemCpuResponse(BaseModel):
    """Gesamtübersicht über CPU-Daten des Systems."""
    # Anzahl der logischen CPUs
    cpu_count: int = 0.0
    # Basis-Statistiken
    cpu_stats: CpuStatsResponse
    # Durchschnittslasten
    cpu_load: CpuLoadResponse
    # Prozentwerte
    cpu_percs: list[float]
    # Zeitstatistiken pro CPU
    cpu_times: list[CpuTimesResponse]
    # Frequenzinformationen pro CPU
    cpu_freqs: list[CpuFreqResponse]


class MemoryVirtualResponse(BaseModel):
    # total physical memory (exclusive swap).
    total: int = 0
    # the memory that can be given instantly to processes without the system going into swap.
    available: int = 0
    # the percentage usage calculated as (total - available) / total * 100.
    percent: int = 0
    # memory used, calculated differently depending on the platform and designed for informational purposes only.
    used: int = 0
    # memory not being used at all (zeroed) that is readily available.
    free: int = 0
    # memory currently in use or very recently used, and so it is in RAM.
    active: int = 0
    # memory that is marked as not used.
    inactive: int = 0
    # cache for things like file system metadata.
    buffers: int = 0
    # cache for various things
    cached: int = 0
    # memory that may be simultaneously accessed by multiple processes.
    shared: int = 0
    # in-kernel data structures cache.
    slab: int = 0
    # memory that is marked to always stay in RAM. It is never moved to disk.
    wired: int = 0


class MemorySwapResponse(BaseModel):
    # total swap memory in bytes
    total: int = 0
    # used swap memory in bytes
    used: int = 0
    # free swap memory in bytes
    free: int = 0
    # the percentage usage calculated as (total - available) / total * 100
    percent: int = 0
    # the number of bytes the system has swapped in from disk (cumulative)
    sin: int = 0
    # the number of bytes the system has swapped out from disk (cumulative)
    sout: int = 0


class SystemMemoryResponse(BaseModel):
    # info for the virtual memory
    virtual: MemoryVirtualResponse
    # info for the swap memory
    swap: MemorySwapResponse


class DiskUsageResponse(BaseModel):
    # referenced device
    device: str = ""
    # total space on the specified disk
    total: int = 0
    # used space on the specified disk
    used: int = 0
    # free space on the specified disk
    free: int = 0
    # free space on the specified disk as percentage
    percent: int = 0


class DiskIoCountersResponse(BaseModel):
    # referenced device
    device: str = ""
    # number of reads
    read_count: int = 0
    # number of writes
    write_count: int = 0
    # number of bytes read
    read_bytes: int = 0
    # number of bytes written
    write_bytes: int = 0
    # time spent reading from disk (in milliseconds)
    read_time: int = 0
    # time spent writing to disk (in milliseconds)
    write_time: int = 0
    #  time spent doing actual I/Os
    busy_time: int = 0
    # number of merged reads
    read_merged_count: int = 0
    # number of merged writes
    write_merged_count: int = 0


class SystemDiskResponse(BaseModel):
    # usage info for all disk partitions
    usage: list[DiskUsageResponse]
    # io counter info for all disk partitions
    io_counters: list[DiskIoCountersResponse]
