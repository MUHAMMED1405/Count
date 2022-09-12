import subprocess
from kivy.config import Config
out = subprocess.run(["xdpyinfo | awk '/dimensions/ {print $2}'", '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8')
screen = out.split('x')
screenw = int(screen[0])
screenh = int(screen[1])
Config.set('graphics', 'width', screenw)
Config.set('graphics', 'height', screenh)
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 0)
numpl = 0
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class count(GridLayout):
    def __init__(self, **kwargs):
        super(count, self).__init__()
        self.cols = 1
        self.rows = 3
        self.press = Button(text="+")
        self.press.background_color = "#0000FF"
        self.press.bind(on_press=self.plus)
        self.press.font_size = 100
        self.add_widget(self.press)
        self.count = Label(text="0")
        self.count.font_size = 100
        self.add_widget(self.count)
        self.pressi = Button(text="-")
        self.pressi.background_color = "#FF0000"
        self.pressi.bind(on_press=self.sub)
        self.pressi.font_size = 100
        self.add_widget(self.pressi)

    def plus(self, instance):
        numpl = int(self.count.text) + 1
        self.count.text = str(numpl)

    def sub(self, instance):
        if self.count.text != "0":
            numpl = int(self.count.text) - 1
            self.count.text = str(numpl)

class Count(App):
    def build(self):
        Window.borderless = True
        return count()
Count().run()
