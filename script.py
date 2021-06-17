#!/usr/bin/env python3

from sys import argv
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
buzzer = GPIO.PWM(17, 500)
buzzer.start(50)

# led
led_red = 26
GPIO.setup(led_red, GPIO.OUT)
# Variables
threshold = int(argv[2])
if threshold > 150:
    threshold = 150
if threshold < 5:
    threshold = 5
initial_frequency = int(argv[1])
if initial_frequency < 5:
    initial_frequency = 5
if initial_frequency > 20000:
    initial_frequency = 20000
# buton resetare -> ctrl c catre script.py
# buton start python3 script.py cu argumente
# sliders and inputbox pentru frequency


def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if dist < threshold:
                buzzer.ChangeFrequency(initial_frequency)
                GPIO.output(led_red, GPIO.HIGH)
                time.sleep(0.5)
            else:
                buzzer.ChangeFrequency(1)
                GPIO.output(led_red, GPIO.LOW)
                time.sleep(0.5)
    finally:
        buzzer.stop()
        GPIO.cleanup()
