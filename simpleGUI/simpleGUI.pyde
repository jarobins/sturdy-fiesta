
class ToolBar:
    def __init__(self):
        pass

class MenuBar:
    def __init__(self):
        pass

class Button:
    def __init__(self, x, y, t, func):
        ''' Button Class
            x, y: position of the button
            func: function to fun when the button is pressed
        '''
        self.x = x
        self.y = y
        self.func = func
        self.t = t
        self.w = 60
        self.h = 30
        
    def mouseOver(self):
        res = False
        if (mouseX > self.x) and (mouseX < (self.x + self.w)):
            res = True
        if (mouseY > self.y) and (mouseY < (self.y + self.h)):
            res &= True
        else:
            res = False
        return res
        
    def render(self):
        stroke(255)
        if self.mouseOver():
            fill(100)
        else:
            fill(10)
        rect(self.x, self.y, 60, 30)
        stroke(0)
        fill(255)
        textAlign(CENTER, CENTER);
        text(self.t, self.x+(self.w/2), self.y+(self.h/2)-1)
        
def print_s():
    print("THIS")
    

b = Button(10, 10, "OK", print_s)


def setup():
    size(600, 600)
    
def draw():
    background(0)
    if mousePressed:
        if b.mouseOver():
            b.func()
    b.render()
    
    
