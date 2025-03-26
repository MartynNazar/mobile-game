from kivy.app import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


def func():
    print("щось робимо")




class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text="це кнопка на першому вікні")
        btn.on_press = self.go_to_second
        self.add_widget(btn)

    def go_to_second(self):
        self.manager.current = "second"


class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text="це кнопка на другому вікні")
        btn.on_press = self.go_to_third
        self.add_widget(btn)


    def go_to_third(self):
        self.manager.current = "third"



class ThirdScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        btn = Button(text="це кнопка на третьому вікні")
        btn.on_press = self.go_to_first

        lbl = Label(text="це надпис")
        lbl_1 = Label(text="це таж надпис")

        self.add_widget(btn)
        self.add_widget(lbl)
        self.add_widget(lbl_1)


    def go_to_first(self):
        self.manager.current = "first"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget((FirstScreen(name="first")))
        sm.add_widget((SecondScreen(name="second")))
        sm.add_widget((ThirdScreen(name="third")))




        return sm

MyApp().run()