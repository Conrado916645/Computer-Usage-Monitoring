import socket

class System_Information:

    def get_machine_name():
        return socket.gethostname()

    @classmethod
    def get_ip_address(cls):
        return socket.gethostbyname(cls.get_machine_name())