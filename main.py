from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line,Rectangle,Triangle,Color
from kivy.core.window import Window
import random

width = 1500
height = 1000
Window.size = (width,height)

class RobotWorld(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.block_size = 100

        with self.canvas:
            for i in range (int((height/self.block_size))):
                for k in range (int((width/self.block_size))):
                    Rectangle(pos=((self.block_size*k),(self.block_size*i)))


game = RobotWorld() # global variable

class RobotApp(App):
    def build(self):
        return game


if __name__ == '__main__':
    RobotApp().run()