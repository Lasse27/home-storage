import psutil
from app.dtos.system_response import *


class _CpuService:

    def get_cpu_times(self) -> list[CpuTimesResponse]:
        util_call: list = psutil.cpu_times(True)
        out_list: list[CpuTimesResponse] = []
        for item in util_call:
            mapped_item: CpuTimesResponse = CpuTimesResponse(
                user=float(getattr(item, "user", 0)),
                nice=float(getattr(item, "nice", 0)),
                system=float(getattr(item, "system", 0)),
                idle=float(getattr(item, "idle", 0)),
                iowait=float(getattr(item, "iowait", 0)),
                irq=float(getattr(item, "irq", 0)),
                softirq=float(getattr(item, "softirq", 0)),
                steal=float(getattr(item, "steal", 0)),
                guest=float(getattr(item, "guest", 0)),
                guest_nice=float(getattr(item, "guest_nice", 0)),
            )
            out_list.append(mapped_item)
        return out_list

    def get_cpu_freqs(self) -> list[CpuFreqResponse]:
        util_call = psutil.cpu_freq(True)
        out_list: list[CpuFreqResponse] = []
        for item in util_call:
            mapped_item: CpuFreqResponse = CpuFreqResponse(
                current=float(getattr(item, "current", 0)),
                min=float(getattr(item, "min", 0)),
                max=float(getattr(item, "max", 0)),
            )
            out_list.append(mapped_item)
        return out_list

    def get_cpu_stats(self) -> CpuStatsResponse:
        util_call = psutil.cpu_stats()
        return CpuStatsResponse(
            ctx_switches=int(getattr(util_call, "total", 0)),
            interrups=int(getattr(util_call, "interrups", 0)),
            soft_interrups=int(getattr(util_call, "soft_interrups", 0)),
            syscalls=int(getattr(util_call, "syscalls", 0)),
        )

    def get_cpu_load(self) -> CpuLoadResponse:
        x, y, z = [x / psutil.cpu_count() * 100.0 for x in psutil.getloadavg()]
        return CpuLoadResponse(
            min_1_load=x,
            min_5_load=y,
            min_15_load=z
        )

    def get_cpu_count(self) -> int:
        util_call: int = psutil.cpu_count()
        return util_call

    def get_cpu_cpu_percs(self) -> list[float]:
        util_call = psutil.cpu_percent(0.1, True)
        return util_call


class _MemoryService:

    def get_virtual_memory(self):
        util_call = psutil.virtual_memory()
        return MemoryVirtualResponse(
            total=int(getattr(util_call, "total", 0)),
            available=int(getattr(util_call, "available", 0)),
            percent=int(getattr(util_call, "percent", 0)),
            used=int(getattr(util_call, "used", 0)),
            free=int(getattr(util_call, "free", 0)),
            active=int(getattr(util_call, "active", 0)),
            inactive=int(getattr(util_call, "inactive", 0)),
            buffers=int(getattr(util_call, "buffers", 0)),
            cached=int(getattr(util_call, "cached", 0)),
            shared=int(getattr(util_call, "shared", 0)),
            slab=int(getattr(util_call, "slab", 0)),
            wired=int(getattr(util_call, "wired", 0))
        )

    def get_swap_memory(self):
        util_call = psutil.swap_memory()
        return MemorySwapResponse(
            total=int(getattr(util_call, "total", 0)),
            used=int(getattr(util_call, "used", 0)),
            free=int(getattr(util_call, "free", 0)),
            percent=int(getattr(util_call, "percent", 0)),
            sin=int(getattr(util_call, "sin", 0)),
            sout=int(getattr(util_call, "sout", 0)),
        )


class _DiskService:
    def get_disk_usages() -> list[DiskUsageResponse]:
        pass

    def get_disk_iocounters() -> list[DiskIoCountersResponse]:
        pass


class SystemService:

    def __init__(self):
        self._cpu_service = _CpuService()
        self._memory_service = _MemoryService()
        self._disk_service = _DiskService()

    def get_full_system_info(self):
        pass

    def get_cpu_info(self):
        cpu_count: int = self._cpu_service.get_cpu_count()
        cpu_stats: CpuStatsResponse = self._cpu_service.get_cpu_stats()
        cpu_load: CpuLoadResponse = self._cpu_service.get_cpu_load()
        cpu_percs: list[float] = self._cpu_service.get_cpu_cpu_percs()
        cpu_freqs: list[CpuFreqResponse] = self._cpu_service.get_cpu_freqs()
        cpu_times: list[CpuTimesResponse] = self._cpu_service.get_cpu_times()
        return SystemCpuResponse(
            cpu_count=cpu_count,
            cpu_stats=cpu_stats,
            cpu_load=cpu_load,
            cpu_percs=cpu_percs,
            cpu_freqs=cpu_freqs,
            cpu_times=cpu_times)

    def get_memory_info(self):
        virtual = self._memory_service.get_virtual_memory()
        swap = self._memory_service.get_swap_memory()
        return SystemMemoryResponse(
            virtual=virtual,
            swap=swap)

    def get_disk_info(self):
        pass

    def get_temperature_info(self):
        pass
