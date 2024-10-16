#20241015 T Mansfield version 0.1
#Script to report back system health checks
#The script uses the python psutil package
#20241015 T Mansfield version 0.2
#Adding in memory and disk usage

import os
import psutil

def get_healthcheck():
#  CPU Usage
	cpu_usage = psutil.cpu_percent(interval=1)
#  Mem Usage
	mem_usage = psutil.virtual_memory()
#  Disk Usage
	disk_usage = psutil.disk_usage('/')

	return {
		'cpu_usage': f'{cpu_usage}%', 
		'memory_usage': f'{mem_usage}%',
		'disk_usage': f'{disk_usage}%'
	}

if __name__ == "__main__":
    print(get_healthcheck())
