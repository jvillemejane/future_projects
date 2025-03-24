# @see : https://www.youtube.com/watch?v=QUHnJrFouv8
# File name must have the same name as the ClassApp
# without App (and lowercase)
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)

    def pressed_button(self):
        print(f'Name: {self.name.text}')


class SecondApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    SecondApp().run()