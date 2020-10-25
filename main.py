from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line,Rectangle,Triangle,Color
from kivy.core.window import Window
import random

width = 1500
height = 1000
Window.size = (width,height)

class Robot(Widget):
    def __init__(self, block_size , **kwargs ):
        super().__init__(**kwargs)
        self.block_size = block_size
        self.column = 0
        self.row = 0
        self.direct = ['w','d','s','a']
        self.direction = 'w'
        self._keyboard = Window.request_keyboard( self._keyboard_closed, self)
        self._keyboard.bind(on_key_down= self._on_keyboard_down)

    def draw (self):
        Color(0,1,0)
        self.player = Triangle(points=[(self.column*self.block_size)+self.block_size/2 , (self.row*self.block_size)+self.block_size , self.column*self.block_size , self.row*self.block_size , (self.column*self.block_size)+self.block_size , self.row*self.block_size])

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        
        if text == 'w':
            self.move()
        elif text == 's':
            self.row -= 1
        elif text == 'd':
            self.turn_right()
        elif text == 'a':
            self.turn_left()

        point1 = [self.column*self.block_size , self.row*self.block_size]
        point2 = [(self.column*self.block_size)+self.block_size/2 , self.row*self.block_size]
        point3 = [(self.column*self.block_size)+self.block_size , self.row*self.block_size]
        point4 = [(self.column*self.block_size)+self.block_size , (self.row*self.block_size)+self.block_size/2]
        point5 = [(self.column*self.block_size)+self.block_size , (self.row*self.block_size)+self.block_size]
        point6 = [(self.column*self.block_size)+self.block_size/2 , (self.row*self.block_size)+self.block_size]
        point7 = [(self.column*self.block_size) , (self.row*self.block_size)+self.block_size]
        point8 = [(self.column*self.block_size) , (self.row*self.block_size)+self.block_size/2]

        self.player.points = [(self.column*self.block_size)+self.block_size/2 , (self.row*self.block_size)+self.block_size , self.column*self.block_size , self.row*self.block_size , (self.column*self.block_size)+self.block_size , self.row*self.block_size]
        if (self.direction == 'w'):
            self.player.points = [point1[0],point1[1],point3[0],point3[1],point6[0],point6[1]]
        elif (self.direction == 'd'): 
            self.player.points = [point1[0],point1[1],point4[0],point4[1],point7[0],point7[1]]
        elif (self.direction == 's'): 
            self.player.points = [point2[0],point2[1],point5[0],point5[1],point7[0],point7[1]]
        elif (self.direction == 'a'): 
            self.player.points = [point3[0],point3[1],point5[0],point5[1],point8[0],point8[1]]
        return True
    
    def turn_right(self):
        for i in range (len(self.direct)):
            if self.direct[i] == self.direction:
                if i == 3:
                    self.direction = self.direct[0]
                else :
                    self.direction = self.direct[i+1]
                break
    def turn_left(self):
        for i in range (len(self.direct)):
            if self.direct[i] == self.direction:
                if i == 0:
                    self.direction = self.direct[3]
                else :
                    self.direction = self.direct[i-1]
                break

    def move(self):
          
        if self.direction == 'w':
            if (self.row*self.block_size)+self.block_size < height :
                self.row += 1
        elif self.direction == 'd':
            if (self.column*self.block_size)+self.block_size < width:
                self.column += 1
        if self.direction == 's':
            if self.row > 0 :
                self.row -= 1
        if self.direction == 'a':
            if self.column > 0  :
                self.column -= 1

class RobotWorld(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.block_size = 100
        self.robot = Robot(self.block_size)

        with self.canvas:
            for i in range (int((height/self.block_size))):
                for k in range (int((width/self.block_size))):
                    Rectangle(pos=((self.block_size*k),(self.block_size*i)))

            self.robot.draw()

game = RobotWorld() # global variable

class RobotApp(App):
    def build(self):
        return game


if __name__ == '__main__':
    RobotApp().run()