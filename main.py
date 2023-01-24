import time
from  turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda boii")
screen.tracer(0)


anaconda = Snake()
food = Food()
scoreboard = Scoreboard()
print(anaconda.snake_pen)



screen.listen()
screen.onkey(anaconda.up, "Up")
screen.onkey(anaconda.down, "Down")
screen.onkey(anaconda.left, "Left")
screen.onkey(anaconda.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    anaconda.move()

# Detect collision with food
    if anaconda.head.distance(food) < 15:
        food.refresh()
        anaconda.extend()
        scoreboard.clear()
        scoreboard.points += 1
        scoreboard.score()

    if anaconda.head.xcor() > 280 or anaconda.head.xcor() < -280 or anaconda.head.ycor() > 280 or anaconda.head.ycor() < -280:
        scoreboard.gmae_over()
        game_on = False


    for segments in anaconda.snake_pen[1:]:
        if anaconda.head.distance(segments) < 10:
            game_on = False
            scoreboard.gmae_over()



























screen.exitonclick()