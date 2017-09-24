import os
os.environ['KIVY_WINDOW'] = 'sdl2'
#import kivy
#kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from Adafruit_BluefruitLE import  get_provider
from Adafruit_BluefruitLE.services import UART


class HypnosApp(App):

    def build(self):
        layout = GridLayout(cols=1, rows=3)
        layout.add_widget(Label(text='Write something:'))
        self.text = TextInput()
        layout.add_widget(self.text)
        self.send_button = Button(text='Send')
        layout.add_widget(self.send_button)
        return layout


if __name__ == '__main__':

    ble = get_provider()
    ble.initialize()
    adapter = ble.get_default_adapter()
    HypnosApp().run()
