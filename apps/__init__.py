import os

from system_information import System_Information as machine
from system_tools import Tools as tool


print('\n-----Computer Usage Monitoring-----\n')
print('Computer name: {name}'.format(name=machine.get_machine_name()))
print('IP Adddress: {ip}'.format(ip=machine.get_ip_address()))
print('Disk Usage: {disk_usage}%'.format(disk_usage=tool.get_disk_usage()))
print('Memory Usage: {memory}%'.format(memory=tool.get_memory_usage()))
print('CPU Usage: {cpu}%\n'.format(cpu=tool.get_cpu_usage()))