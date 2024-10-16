#20241015 T Mansfield version 0.1
#Script to report back system health checks
#The script uses the python psutil package
#20241015 T Mansfield version 0.2
#Adding in memory and disk usage
#20241016 T Mansfield version 0.3
#Changing output to JSON
#20241016 T Mansfield 
#Adding  endpoints
#Adding app.run (0.0.0.0) to allow running in a container
import os
import psutil
from  flask import Flask, jsonify

app = Flask(__name__)
@app.route('/healthcheck', methods=['GET'])

def get_healthcheck():
# CPU Usage
	cpu_usage = psutil.cpu_percent(interval=1)
# Memory usage
	mem_usage = psutil.virtual_memory()
# Disk Usage
	disk_usage =  psutil.disk_usage('/')

	return jsonify({'CPU_usage': f'{cpu_usage}%',
		'Mem_usage': f'{mem_usage}%',
		'Disk_usage': f'{disk_usage}%'
	})


if __name__ == "__main__":
#        app.run(debug=True)
	app.run(host='0.0.0.0', port=5000)
#To test use curl http://localhost:5000/healthcheck
