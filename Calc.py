from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set("graphics", "width", "640")
Config.set("graphics", "height", "480")


def btn_press(a, calc=0):
    a.background_color = [178 / 255, 102 / 255, 255 / 255, 1]
    calc += 1


class MyApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        bl = BoxLayout(orientation="vertical", spacing=2)
        self.add_widget(bl)
        bl.add_widget(Label(text="Как изменилась цена, если свеча закрашенная?", ))
        b1 = (Button(text="стоимость акции уменьшилась",
                     on_press=btn_press,
                     background_normal=" ",
                     background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2 = (Button(text="стоимость акции увеличилась",
                     on_press=btn_press,
                     background_normal=" ",
                     background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b3 = (Button(text="стоимость акции не изменилась",
                     on_press=btn_press,
                     background_normal=" ",
                     background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b4 = (Button(text="стоимость акции стала равна нулю",
                     on_press=btn_press,
                     background_normal=" ",
                     background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b5 = (Button(text="Ответить",
                     on_press=lambda x: set_screen("app2"),
                     background_normal=" ",
                     background_color=[155 / 255, 142 / 255, 156 / 255, 1]))
        bl.add_widget(b1)
        bl.add_widget(b2)
        bl.add_widget(b3)
        bl.add_widget(b4)
        bl.add_widget(b5)


class MyApp2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b2 = BoxLayout(orientation="vertical", spacing=2)
        self.add_widget(b2)
        b2.add_widget(Label(text="Как изменилась цена, если свеча прозрачная?", ))

        b2.add_widget(Button(text="стоимость акции увеличилась",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="стоимость акции уменьшилась",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="стоимость акции не изменилась",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="стоимость акции стала равна нулю",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="Ответить",
                             on_press=lambda x: set_screen("app3"),
                             background_normal=" ",
                             background_color=[155 / 255, 142 / 255, 156 / 255, 1]))


class MyApp3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b2 = BoxLayout(orientation="vertical", spacing=2)
        self.add_widget(b2)
        b2.add_widget(Label(text="Как изменилась цена, если свеча в виде абсолютного креста?", ))

        b2.add_widget(Button(text="стоимость акции увеличилась",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="стоимость акции уменьшилась",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="стоимость акции не изменилась",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="стоимость акции изменилась не более чем на два шага цены",
                             on_press=btn_press,
                             background_normal=" ",
                             background_color=[8 / 255, 142 / 255, 156 / 255, 1]))
        b2.add_widget(Button(text="Ответить",
                             on_press=lambda x: set_screen("app4"),
                             background_normal=" ",
                             background_color=[155 / 255, 142 / 255, 156 / 255, 1]))


sm = ScreenManager()
sm.add_widget(MyApp(name="app"))
sm.add_widget(MyApp2(name="app2"))
sm.add_widget(MyApp3(name="app3"))


def set_screen(name_screen):
    sm.current = name_screen


class Run(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return sm


if __name__ == "__main__":
    Run().run()
