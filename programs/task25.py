'''
write a script to display the below information 

1. CPU percentage
2. Memory info ( total memory, available, used)
3. process info
4. disk partitions
5. network statistics
4. platform details ( like OS name , model , python version)
5. boot time of your system
6. IP Address of your system
7. hostname of the system

'''

import psutil
import platform
print(psutil.cpu_percent(interval=1))
print(psutil.virtual_memory())
print(psutil.disk_partitions())
print(psutil.net_connections())
print(platform.platform())
print(platform.python_version())