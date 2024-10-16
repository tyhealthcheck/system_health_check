# system_health_check
20241016 T Mansfield
This a program in python to do a simple healthcheck
It will use the psutil project to interrogate the local system

20241016 T Mansfield
The ty_system_healthcheck.py script uses psutils and flask libraies to get and retreive information from the localserver upon which it is run.
psutils is used to get cpu usage, memory usage and disk usage which is returned as a float number
flask is used to create a api which allows the program to run in the background and services request through using the /healthcheck
e.g. https://127.0.0.1:5000/healthcheck.

To run as a container the Dockerfile has been uploaded - this file create the ty_system_healthcheck container.  It installs the latest ubuntu images followed by a python3 install.  After the python3 install the psutil and flask modules are installed.
The ty_system_healthcheck.py is executed. 

To run the the ty_system_healthcheck.py in a container.  Assuming that the docker engine is running:
>docker build -t ty_system_healthcheck .
>docker image        #to check if the image has been built successfully
>docker run ty_system_healthcheck

when running open a seperate terminal window on the same server and use:
curl http://<private ip address>:5000/healthcheck.
It returns the cpu usage, memory useage and disk usage.

While testing for connection, the python file run straight from the terminal window will return info on 127.0.0.1:5000/healthcheck
but inside a contained it is unable to find the local server (as it's in a container I guess).  The app.run() method was changed to app.run('0.0.0.0', port=5000)
which allows for the local private ip address to be used.

The app.run method also allows for debugging by passing the debug=true parameter.  Useful for identifying runtime errors.

Time constraints have limited the testing but an element was done during compliation and runtime
