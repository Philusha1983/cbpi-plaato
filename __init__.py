# -*- coding: utf-8 -*-
import urllib2

from modules import cbpi
from modules.core.hardware import SensorActive
from modules.core.props import Property
import json

PINS = {
    "Percent of beer left": "v48"
}

plaato_base_url = 'http://plaato.blynk.cc'


@cbpi.sensor
class PlaatoSensor(SensorActive):
    pins = []
    for key in PINS.keys():
        pins.append(key)

    api_key = Property.Text("Api Key", configurable=True)
    pin = Property.Select(
        "Pin", options=pins, description="Select which metric you want to listen for")
    refresh_time = Property.Text(
        "Refresh Time", default_value="5", configurable=True)

    def get_unit(self):
        if self.pin == "Percent of beer left":
            return "% Beer left"
        else:
            return ""

    def execute(self):
        while self.is_running():
            pin_value = PINS[self.pin]
            refresh = float(self.refresh_time)
            response = self.get(pin_value)

            rounded_response = str(round(float(response), 2))

            self.data_received(rounded_response)
            self.api.socketio.sleep(refresh)

    def get(self, pin):
        url = "{0}/{1}/get/{2}".format(plaato_base_url, self.api_key, pin)
        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, error:
            err = error.read()
            print err
        else:
            content = response.read()
            j = json.loads(content)

            if type(j) == list:
                return j[0]
            else:
                return j
