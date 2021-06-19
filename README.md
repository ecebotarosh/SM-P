# Social Distancing Enforcer
This is a project that enforces social distancing norms.

## How to use
* Create a new user `pi` or modify the `configurer.sh` script in order give your user the required privileges in order to be able to run the script as non-root.
* Either grant the user `pi` administrative privileges and run the `configurer.sh` script or run the script as root.
* Revoke the administrative privileges from the user `pi`
* Create a virtual environment using Python 3.8 (Python 3.9 is not currently supported)
* `pip install -r requirements.txt`
* `./app.py`

Now you have a web server running on port 8080 that hosts a web application that controls the Raspberry Pi.
You can change the buzzer frequency, configure the distance at which it starts to buzz or turn the device on and off.
