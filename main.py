import os
os.environ['KIVY_WINDOW'] = 'sdl2'
#import kivy
#kivy.require('1.0.6')

from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 200)
#from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from Adafruit_BluefruitLE import  get_provider
from Adafruit_BluefruitLE.services import UART

def btconnect_hypnos():
    ble = get_provider()
    ble.initialize()
    adapter = ble.get_default_adapter()
    try:
        adapter.start_scan()
        device = UART.find_device()
        if device is None:
            raise RuntimeError("No device")
    finally:
        adapter.stop_scan()
    device.connect()
    return device

class HypnosApp(App):
    kv_directory = 'templates'
    def build(self):
         pass
     
    def send_data(self, cmd):
        print(cmd)


if __name__ == '__main__':
    HypnosApp().run()
