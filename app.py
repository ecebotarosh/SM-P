#!/usr/bin/env python3.8
 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from uvicorn import run
from os import environ
from subprocess import Popen, PIPE
 
content = """
<!DOCTYPE html>
<html>
<head>
<title>Hello World</title>
</head>
<body>
<p>Hello, World!</p>
</body>
</html>
"""

with open('index.html') as f:
    content = f.read()
 
 
app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
RPI_CONTROLLER_SCRIPT_PATH = "/home/pi/script.py"
 
 
 
def spawn():
    if environ["state"]=="OFF":
        process = Popen([RPI_CONTROLLER_SCRIPT_PATH, environ['frequency'], environ['threshold']], shell=False, stdout=PIPE, stderr=PIPE)
        environ["PID"]=str(process.pid)
        environ["state"]="ON"
    
 
 
def kill():
    if environ["state"]=="ON":
        Popen(['kill', '-9', environ['PID']], shell=False)
        environ["state"]="OFF"
 
 
def reset():
    kill()
    spawn()
 
 
@app.get('/', response_class=HTMLResponse)
def index():
    return content
 
 
@app.get('/app/frequency/{freq}', response_class=HTMLResponse)
def changeFrequency(freq : int):
    if freq>20000:
        freq=20000
    if freq<=5:
        freq = 5
    environ["frequency"]=str(freq)
    if environ["state"]=="ON":
        reset()
    return content
 
 
@app.get('/app/frequency')
def showFrequency():
    return {'freq' : int(environ["frequency"])}
 
 
@app.get('/app/state/on', response_class=HTMLResponse)
def startup():
    spawn()
    return content
 
@app.get('/app/state/off', response_class=HTMLResponse)
def shutdown():
    kill()
    return content
 
 
@app.get('/app/threshold/{threshold}', response_class=HTMLResponse)
def setThreshold(threshold : int):
    if threshold > 150:
        threshold = 150
    if threshold < 5:
        threshold = 5
    environ["threshold"] = str(threshold)
    if environ["state"]=="ON":
        reset()
    return content
 
@app.get('/app/threshold')
def getThreshold():
    return {'threshold':int(environ["threshold"])}
 
if __name__=="__main__":
    environ["frequency"] = "500"
    environ["state"]="OFF"
    environ["threshold"] = "100"
    run(app, host='0.0.0.0', port=8080)
