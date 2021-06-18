#!/usr/bin/python

from flask import request, jsonify
from flask_api import FlaskAPI
#from flask_cors import CORS
#import RPi.GPIO as GPIO

timeStamp = "20:50:25"
gps = "Lat: 45.766 Long: 667.555"
lux = 2000
white = 46
red = 107
green = 160
blue = 120
clear = 56
tempColor = 600
temp = 27
press = 850
hum = 408

app = FlaskAPI(__name__)
#CORS(app)

@app.route('/', methods=["GET"])
def api_root():
    return jsonify([{"Bienvenido a la plataforma Citemetrix."}])
  
@app.route('/sensors/VEML7700', methods=["GET","POST"])
def api_veml7700():
    global timeStamp, gps, lux, white 
    if request.method == "GET":
        response = jsonify([{'GPS': gps, "Timestamp": timeStamp, 'lux': lux, 'white': white}]) 
        response.headers.add("Access-Control-Allow-Origin", "https://keen-wescoff-53ef2d.netlify.app")
        return response
    else:
        timeStamp = str(request.data.get("timeStamp"))
        gps = str(request.data.get("gpsData"))
        lux = str(request.data.get("lux"))
        white = str(request.data.get("white"))
        return jsonify([{'Status': 'OK'}])

@app.route('/sensors/TCS34725', methods=["GET","POST"])
def api_tcs34725():
    global timeStamp, gps, red, green, blue, clear, tempColor 
    if request.method == "GET":
        response = jsonify([{'GPS': gps, 'Timestamp': timeStamp, 'red': red, 'green': green, 'blue': blue, 'clear': clear, 'tempColor': tempColor}]) 
        response.headers.add("Access-Control-Allow-Origin", "https://keen-wescoff-53ef2d.netlify.app")
        return response

    else:
        timeStamp = str(request.data.get("timeStamp"))
        gps = str(request.data.get("gpsData"))
        red = str(request.data.get("red"))
        green = str(request.data.get("green"))
        blue = str(request.data.get("blue"))
        clear = str(request.data.get("clear"))
        tempColor = str(request.data.get("tempColor"))
        return jsonify([{'Status': 'OK'}])

@app.route('/sensors/BME680', methods=["GET"])
def api_bme680():
    global timeStamp, gps, temp, press, hum
    if request.method == "GET":
        response = jsonify([{'GPS': gps, 'Timestamp': timeStamp, 'temperatura': temp, 'presion': press}])
        response.headers.add("Access-Control-Allow-Origin", "https://keen-wescoff-53ef2d.netlify.app")
        return response
    else:
        timeStamp = str(request.data.get("timeStamp"))
        gps = str(request.data.get("gpsData"))
        temp = str(request.data.get("temperatura"))
        press = str(request.data.get("presion"))
        hum = str(request.data.get("humedad"))
        return jsonify([{'Status': 'OK'}])


if __name__ == "__main__":
    app.run()
