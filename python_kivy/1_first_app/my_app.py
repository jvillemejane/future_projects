# @see : https://www.youtube.com/watch?v=QUHnJrFouv8
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='First Name: '))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Last Name: '))
        self.last_name = TextInput(multiline=False)
        self.add_widget(self.last_name)

        self.button_1 = Button(text="Test", font_size=40)
        self.button_1.bind(on_press=self.pressed_button)
        self.add_widget(self.button_1)

    def pressed_button(self, instance):
        name = self.name.text
        print(f'Pressed {name}')

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()