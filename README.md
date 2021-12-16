# IoT based smart Energy management system

This project is about analyzing power usage in real time
using IoT. We created a website using thingspeak and hosted it
online using Ngrok. Data is acquired from different sensors and
processed in Arduino & Raspberry pi.

## Group members

- [@saijyothikumar](mailto:saijyothikumar.s18@iiits.in)

- [@charanreddy](mailto:charanreddy.t18@iiits.in)

## Code links

- [Project_codes](https://drive.google.com/drive/folders/1qY_Tj0fDwJMy6e0F-GDmlmHWtbFn1JxQ?usp=sharing)

## Table of Contents

- __btp_arduino_code__ 
    - Instantaneous power measurment
    - Arduino raspberry pi communication
    - Control of electronic device
    - Auto on and off of water pump
    - GSM module
- __btp_temprature_regulation__
    - Code to automatically control fan speed based on parameter set on website and temperature measured by lm35
- __btp_water_level_using_ultrasonic__
    - Code related to automatically turning on and off of water pump based on water level in tank
- __btp_raspberry_code__
    - main code of raspberry pi and calculates power units consumed based on instantaneous power by arrduino
    - sends mail
    - uploads and downloads data from thingspeak
- __btp_project_website__
    - Code for complete website including database and templates for website
