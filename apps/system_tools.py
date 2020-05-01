import psutil

class Tools:

    def get_disk_usage():
        return psutil.disk_usage('/').percent

    def get_cpu_usage():
        return psutil.cpu_percent(interval=1)

    def get_memory_usage():
        return psutil.swap_memory().percent
