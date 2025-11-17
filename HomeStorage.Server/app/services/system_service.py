import psutil
from app.dtos.system_response import *


class _CpuService:

    def get_cpu_times(self) -> list[CpuTimesResponse]:
        # Helper function
        def _map_cpu_time(item) -> CpuTimesResponse:
            mapped_item = CpuTimesResponse()
            try:
                mapped_item.user = item[0]
                mapped_item.nice = item[1]
                mapped_item.system = item[2]
                mapped_item.idle = item[3]
                mapped_item.iowait = item[4]
                mapped_item.irq = item[5]
                mapped_item.softirq = item[6]
                mapped_item.steal = item[7]
                mapped_item.guest = item[8]
                mapped_item.guest_nice = item[8]
            except:
                pass
            finally:
                return mapped_item

        # Main function
        util_call: list = psutil.cpu_times(True)
        out_list: list[CpuTimesResponse] = []
        for item in util_call:
            mapped_item: CpuTimesResponse = _map_cpu_time(item=item)
            out_list.append(mapped_item)
        return out_list

#

    def get_cpu_freqs(self) -> list[CpuFreqResponse]:
        # Helper function
        def _map_cpu_freq(item) -> CpuFreqResponse:
            mapped_item = CpuFreqResponse()
            try:
                mapped_item.current = item[0]
                mapped_item.min = item[1]
                mapped_item.max = item[2]
            except:
                pass
            finally:
                return mapped_item

        # Main function
        util_call = psutil.cpu_freq(True)
        out_list: list[CpuFreqResponse] = []
        for item in util_call:
            mapped_item: CpuFreqResponse = _map_cpu_freq(item=item)
            out_list.append(mapped_item)
        return out_list

#

    def get_cpu_stats(self) -> CpuStatsResponse:
        util_call = psutil.cpu_stats()
        mapped_item = CpuStatsResponse()
        try:
            mapped_item.ctx_switches = util_call[0]
            mapped_item.interrups = util_call[1]
            mapped_item.soft_interrups = util_call[2]
            mapped_item.syscalls = util_call[3]
        except:
            pass
        finally:
            return mapped_item

#

    def get_cpu_load(self) -> CpuLoadResponse:
        x1, x2, x3 = [
            x / psutil.cpu_count() * 100.0 for x in psutil.getloadavg()]
        return CpuLoadResponse(
            min_1_load=x1,
            min_5_load=x2,
            min_15_load=x3
        )

#

    def get_cpu_count(self) -> int:
        util_call: int = psutil.cpu_count()
        return util_call

#

    def get_cpu_cpu_percs(self) -> list[float]:
        util_call = psutil.cpu_percent(0.1, True)
        return util_call


class _MemoryService:

    def get_virtual_memory(self):
        util_call = psutil.virtual_memory()
        mapped_item = MemoryVirtualResponse()
        try:
            mapped_item.total = util_call[0]
            mapped_item.available = util_call[1]
            mapped_item.percent = util_call[2]
            mapped_item.used = util_call[3]
            mapped_item.free = util_call[4]
            mapped_item.active = util_call[5]
            mapped_item.inactive = util_call[6]
            mapped_item.buffers = util_call[7]
            mapped_item.cached = util_call[8]
            mapped_item.shared = util_call[9]
            mapped_item.slab = util_call[10]
            mapped_item.wired = util_call[11]
        except:
            pass
        finally:
            return mapped_item

#

    def get_swap_memory(self):
        util_call = psutil.swap_memory()
        mapped_item = MemorySwapResponse()
        try:
            mapped_item.total = util_call[0]
            mapped_item.used = util_call[1]
            mapped_item.free = util_call[2]
            mapped_item.percent = util_call[3]
            mapped_item.sin = util_call[4]
            mapped_item.sout = util_call[5]
        except:
            pass
        finally:
            return mapped_item


class SystemService:

    def __init__(self):
        self.cpu_service = _CpuService()
        self.memory_service = _MemoryService()

    def get_full_system_info(self):
        pass

    def get_cpu_info(self):
        cpu_count: int = self.cpu_service.get_cpu_count()
        cpu_stats: CpuStatsResponse = self.cpu_service.get_cpu_stats()
        cpu_load: CpuLoadResponse = self.cpu_service.get_cpu_load()
        cpu_percs: list[float] = self.cpu_service.get_cpu_cpu_percs()
        cpu_freqs: list[CpuFreqResponse] = self.cpu_service.get_cpu_freqs()
        cpu_times: list[CpuTimesResponse] = self.cpu_service.get_cpu_times()

        return SystemCpuResponse(
            cpu_count=cpu_count,
            cpu_stats=cpu_stats,
            cpu_load=cpu_load,
            cpu_percs=cpu_percs,
            cpu_freqs=cpu_freqs,
            cpu_times=cpu_times
        )

    def get_disk_info(self):
        pass

    def get_memory_info(self):
        virtual = self.memory_service.get_virtual_memory()
        swap = self.memory_service.get_swap_memory()
        return SystemMemoryResponse(
            virtual=virtual,
            swap=swap
        )

    def get_temperature_info(self):
        pass
