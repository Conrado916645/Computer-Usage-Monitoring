from system_information import System_Information as machine

print('\n-----Computer Usage Monitoring-----\n')
print('Computer name: {name}'.format(name=machine.get_machine_name()))
print('Operating System: {os} {version}'.format(
    os=machine.get_operating_system(), version=machine.get_machine_version()))
print('Computer Processor: {cpu}'.format(cpu=machine.get_processor()))
print('IP Adddress: {ip}'.format(ip=machine.get_ip_address()))
print('Disk Usage: {disk_usage}%'.format(disk_usage=machine.get_disk_usage()))
print('Memory Usage: {memory}%'.format(memory=machine.get_memory_usage()))
print('CPU Usage: {cpu}%\n'.format(cpu=machine.get_cpu_usage()))