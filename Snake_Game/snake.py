from turtle import Turtle
SEG_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SEG_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        tt = Turtle("square")
        tt.color("white")
        tt.penup()
        tt.goto(position)
        self.segments.append(tt)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            nx = self.segments[seg_no - 1].xcor()
            ny = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(nx, ny)
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake() 
        self.head = self.segments[0]
