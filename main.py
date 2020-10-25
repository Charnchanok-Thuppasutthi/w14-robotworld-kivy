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
        if self.is_blocked() == False:

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

    def is_blocked(self):

        check = False

        for i in game.wall:
            if self.direction == 'w':
                if (i.row == self.row+1) and (i.column == self.column):
                    check = True
                
            elif self.direction == 'd':
                if (i.row == self.row) and (i.column == self.column+1):
                    check = True
                 
            elif self.direction == 's':
                if (i.row == self.row-1) and (i.column == self.column):
                    check = True
                
            elif self.direction == 'a':
                if (i.row == self.row) and (i.column == self.column-1):
                    check = True
        return check

class Wall (Widget):
    def __init__(self, column , row ,block_size ,**kwargs):
        super().__init__(**kwargs)
        self.block_size = block_size
        self.column = column
        self.row = row

    def draw(self):
        Color(0,0,0)
        Rectangle(pos = (self.column * self.block_size,self.row * self.block_size))

class Target (Widget):
    def __init__(self, column , row ,world_block, **kwargs):
        super().__init__(**kwargs)
        self.column = column
        self.row = row
        self.world_block = world_block

    def draw(self):
        Color(1,0,0)
        self.tar = Rectangle(pos=[(self.world_block*0.25)+(self.world_block*self.column),(self.world_block*0.25) +(self.world_block*self.row)],size=[self.world_block*0.5,self.world_block*0.5])


class RobotWorld(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.block_size = 100
        self.robot = Robot(self.block_size)
        self.wall = []
        self.target = Target(random.randint(0,int((width/self.block_size)-1)),random.randint(0,int((height/self.block_size)-1)),self.block_size)

        for i in range (20):
            self.wall.append(Wall(random.randint(0,int((width/self.block_size)-1)),random.randint(0,int((height/self.block_size)-1)),self.block_size))
        for j in range (len(self.wall)):
            if (self.wall[j].row == self.target.row and self.wall[j].column == self.target.column) or (self.wall[j].column == self.robot.column and self.wall[j].row == self.robot.row):
                self.wall[j] = Wall(random.randint(0,int((width/self.block_size)-1)),random.randint(0,int((height/self.block_size)-1)),self.block_size)
        
        with self.canvas:
            for i in range (int((height/self.block_size))):
                for k in range (int((width/self.block_size))):
                    Rectangle(pos=((self.block_size*k),(self.block_size*i)))

            for j in range (len(self.wall)):
                self.wall[j].draw()

            self.robot.draw()
            self.target.draw()

game = RobotWorld() # global variable

class RobotApp(App):
    def build(self):
        return game


if __name__ == '__main__':
    RobotApp().run()