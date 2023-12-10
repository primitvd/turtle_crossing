from turtle import Turtle, Screen
import random
from cars import Car
import time

screen = Screen()
screen.tracer(0)

t = Turtle()


t.shape("turtle")
t.penup()
t.setheading(90)
t.goto(0,-250)
screen.update()
screen.tracer(1)

screen.onkey(lambda : t.sety(t.ycor() + 50), "Up")
screen.onkey(lambda : t.sety(t.ycor() - 20), "Down")
screen.onkey(lambda : t.setx(t.xcor() + 20), "Right")
screen.onkey(lambda : t.setx(t.xcor() - 20), "Left")
screen.listen()

# screen.update()


t1 = time.time()
t2 = time.time()

cars = []
i = 0
collision = 0
while (t.ycor() < 250 and collision == 0):
    if time.time() - t2 > 5:
        screen.tracer(0)
        for lane in range(5):
            if random.randint(0,1) == 0:
                c =  Car(lane%2, lane)
                cars.append(c)
        t2 = time.time()
    if time.time() - t1 > 0.5:
        for car in cars:
            car.forward(10)
            screen.update()
            if car.distance(t) < 20:
                collision = 1
                screen.tracer(1)
                t.write("Game Over", align="center", font=("Arial", 20, "normal"))
                screen.update()
                break
            # screen.tracer(1)
        t1 = time.time()
    # i += 1
    # print(i)
    # screen.update()

screen.exitonclick()

print(t)