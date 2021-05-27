import turtle
import PIL
from turtle import Shape, TurtleScreen, TurtleGraphicsError
from os.path import isfile

# Methods shouldn't do `if name.lower().endswith(".gif")` but simply pass
# file name along and let it break during image conversion if not supported.

def register_shape(self, name, shape=None):  # call addshape() instead for original behavior
    if shape is None:
        shape = Shape("image", self._image(name))
    elif isinstance(shape, tuple):
        shape = Shape("polygon", shape)

    self._shapes[name] = shape

TurtleScreen.register_shape = register_shape

def __init__(self, type_, data=None):
    self._type = type_

    if type_ == "polygon":
        if isinstance(data, list):
            data = tuple(data)
    elif type_ == "image":
        if isinstance(data, str):
            if isfile(data):
                data = TurtleScreen._image(data) # redefinition of data type
    elif type_ == "compound":
        data = []
    else:
        raise TurtleGraphicsError("There is no shape type %s" % type_)

    self._data = data

Shape.__init__ = __init__

from turtle import Screen, Turtle
import patch_turtle_image

screen = Screen()
screen.bgpic('/Users/kek/Downloads/IMG_6389.JPG')
screen.register_shape('/Users/kek/Downloads/IMG_6398-min.PNG')
turtle = Turtle('/Users/kek/Downloads/IMG_6398-min.PNG')
turtle.pensize(width=20)
turtle.width(width=15)
turtle.pencolor('pink')

border = 1
w = 75 # letter width
h = 150 # letter height
n = w/2 #space
m = h/4

turtle.speed('slow')

turtle.left(90)

turtle.pu()
turtle.goto(-200,150)
turtle.down()

def space():
    turtle.goto(turtle.xcor()+n, turtle.ycor())
    turtle.down()

def space_2():
    turtle.goto(turtle.xcor() + n/2, turtle.ycor())
    turtle.down()

#letter H
def H():
    turtle.goto(turtle.xcor(), turtle.ycor() + h)
    turtle.goto(turtle.xcor(), turtle.ycor() - h / 2)
    turtle.goto(turtle.xcor()+w, turtle.ycor())
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor() - h / 2)
    turtle.down()
    turtle.goto(turtle.xcor(), turtle.ycor() + h )
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor() - h )

#letter A
def A():
    turtle.down()
    turtle.goto(turtle.xcor() + w/2, turtle.ycor() + h)
    turtle.goto(turtle.xcor() + w/2, turtle.ycor() - h)
    turtle.pu()
    turtle.goto(turtle.xcor() - w / 4, turtle.ycor() + h / 2)
    turtle.down()
    turtle.goto(turtle.xcor() - w / 2, turtle.ycor())
    turtle.pu()
    turtle.goto(turtle.xcor() + w/1.5, turtle.ycor() - h/2)

def P():
    turtle.goto(turtle.xcor(), turtle.ycor()+h)
    turtle.right(90)
    turtle.speed('fastest')
    turtle.circle(-w/2, 180, 180)
    turtle.speed('slow')
    turtle.pu()
    turtle.right(90)
    turtle.goto(turtle.xcor() + w/2, turtle.ycor() - h/2)

def Y():
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor()+h)
    turtle.down()
    turtle.goto(turtle.xcor()+w/2, turtle.ycor() - h/3)
    turtle.goto(turtle.xcor() + w / 2, turtle.ycor() + h / 3)
    turtle.pu()
    turtle.goto(turtle.xcor() - w / 2, turtle.ycor() - h / 3)
    turtle.down()
    turtle.goto(turtle.xcor(), turtle.ycor() - h / 1.5)

def B():
    turtle.goto(turtle.xcor(), turtle.ycor() + h)
    turtle.right(90)
    turtle.speed('fastest')
    turtle.circle(-w/3, 180, 180)
    turtle.right(180)
    turtle.circle(-w / 1.5, 180, 180)
    turtle.speed('slow')
    turtle.pu()
    turtle.right(90)
    turtle.goto(turtle.xcor()+w/2, turtle.ycor())

def I():
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor() + h)
    turtle.down()
    turtle.goto(turtle.xcor() + w, turtle.ycor())
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor() - h)
    turtle.down()
    turtle.goto(turtle.xcor() - w, turtle.ycor())
    turtle.pu()
    turtle.goto(turtle.xcor() + w / 2, turtle.ycor())
    turtle.down()
    turtle.goto(turtle.xcor(), turtle.ycor() + h)
    turtle.pu()
    turtle.goto(turtle.xcor()+w/2, turtle.ycor() - h)
    turtle.right(90)

def R():
    turtle.goto(turtle.xcor(), turtle.ycor() + h)
    turtle.speed('fastest')
    turtle.circle(-h / 3, 180, 180)
    turtle.speed('slow')
    turtle.right(180)
    turtle.goto(turtle.xcor()+w/2, turtle.ycor() - h/3)
    turtle.pu()
    turtle.right(90)

def T():
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor()+h)
    #turtle.right(90)
    turtle.down()
    turtle.goto(turtle.xcor() + w, turtle.ycor())
    turtle.pu()
    turtle.goto(turtle.xcor() - w/2 , turtle.ycor())
    turtle.down()
    turtle.goto(turtle.xcor(), turtle.ycor() - h)
    turtle.pu()
    turtle.goto(turtle.xcor() + w/2, turtle.ycor())

def D():
    turtle.goto(turtle.xcor(), turtle.ycor()+h)
    turtle.left(90)
    turtle.speed('fastest')
    turtle.circle(-w, 180, 180)
    turtle.speed('slow')
    turtle.pu()
    turtle.left(90)
    turtle.goto(turtle.xcor() + w, turtle.ycor())

def V():
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor()+h)
    turtle.down()
    turtle.goto(turtle.xcor() + w / 2, turtle.ycor() - h)
    turtle.goto(turtle.xcor() + w / 2, turtle.ycor() + h)
    turtle.pu()
    turtle.goto(turtle.xcor(), turtle.ycor() - h)

def M():
    turtle.goto(turtle.xcor(), turtle.ycor() + h )
    turtle.goto(turtle.xcor() + w / 2, turtle.ycor() - h/2)
    turtle.goto(turtle.xcor() + w / 2, turtle.ycor() + h/2)
    turtle.goto(turtle.xcor(), turtle.ycor() - h)


print(H(), space(), A(), space(), P(), space(), P(), space(), Y())



turtle.pu()
turtle.goto(-300,turtle.ycor()-h-m)
turtle.down()


print(B(), space_2(), I(), space_2(), R(), space_2(), T(), space_2(), H(), space_2(), D(), space_2, A(), space_2(), Y())

turtle.pu()
turtle.goto(-250,turtle.ycor()-h-m)
turtle.down()


print(V(), space(), A(), space(), D(), space(), I(), space(), M())

turtle.pu()
turtle.goto(0,-150)


screen.exitonclick()


