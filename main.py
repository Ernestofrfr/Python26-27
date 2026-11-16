from myFunctions import*
from random import*

turtle.tracer(0)

turtle.colormode(255)

turtle.bgcolor("yellow")
num = randint(10, 200)
distance = randint(-200,300)

angle = randint(10,144)
for times in range( num ):
  
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  border = "cyan"
  fill = (r,g,b)
  bob.color(fill)
  bob.left(72)
  radius = randint(-15, 10)
  bob.forward(times+4*6)
  comet(times + 4 *7, angle)  
  polygon(3, 100,fill)

comet


for times in range( num ):
  
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  border = "cyan"
  fill = (r,g,b)
  bob.color(fill)
  bob.left(72)
  radius = randint(-15, 10)
  bob.forward(times+4*6)
  comet(times + 4 *7, angle)  
  polygon(3, 100,fill)
  
