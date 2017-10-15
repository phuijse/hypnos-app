import os   
os.environ['KIVY_WINDOW'] = 'sdl2'
# import kivy
# kivy.require('1.0.6')
# from numpy as np    
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width', 400)
Config.set('graphics', 'height', 200)
# from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import uuid
from Adafruit_BluefruitLE import  get_provider
from Adafruit_BluefruitLE.services import UART
import atexit

ble = get_provider()
UART_SERVICE_UUID = uuid.UUID('6E400001-B5A3-F393-E0A9-E50E24DCCA9E')

def btconnect_hypnos():
    ble.clear_cached_data()
    #adapter = ble.get_default_adapter()
    adapter = ble.list_adapters()[1]
    print("using adapter %s" %(adapter.name))
    #adapter.power_on()
    ble.disconnect_devices([UART_SERVICE_UUID])
    adapter.start_scan(timeout_sec=10)
    atexit.register(adapter.stop_scan)
    print('Searching for UART devices...')
    device = ble.find_device(service_uuids=[UART_SERVICE_UUID])
    #adapter.stop_scan()
    print(device.name)
    print(device.id)
        #if found is None:
        #    raise RuntimeError("No device")
    return device

class HypnosApp(App):
    kv_directory = 'templates'
    def build(self):
        self.device = btconnect_hypnos()
        self.device.connect()
        UART.discover(self.device)
        self.uart = UART(self.device)
     
    def send_data(self, cmd):
        print(cmd)
        self.uart.write(cmd)
    
    def on_stop(self):
        self.device.disconnect()


if __name__ == '__main__':
    ble.initialize()
    ble.run_mainloop_with(btconnect_hypnos)
#    self.device = btconnect_hypnos()
    #HypnosApp().run()
