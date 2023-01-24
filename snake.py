
from  turtle import Turtle

SNAKE_SEGMENT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_pen = []
        self.create_snake()
        self.head = self.snake_pen[0]

    def create_snake(self):
        for seg in SNAKE_SEGMENT:
            self.add_segment(seg)

    def add_segment(self, seg):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(seg)
        self.snake_pen.append(new_segment)


    def extend(self):
        self.add_segment(self.snake_pen[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_pen) - 1, 0, -1):
            new_x = self.snake_pen[seg_num - 1].xcor()
            new_y = self.snake_pen[seg_num - 1].ycor()
            self.snake_pen[seg_num].goto((new_x), (new_y))
        self.head.forward(MOVE_DISTANCE)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


