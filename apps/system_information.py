import socket
import platform
from system_tools import Tools

class System_Information(Tools):

    def get_machine_name():
        return socket.gethostname()

    @classmethod
    def get_ip_address(cls):
        return socket.gethostbyname(cls.get_machine_name())

    def get_machine_version():
        return platform.version()

    def get_operating_system():
        return platform.system()

    def get_processor():
        return platform.processor()