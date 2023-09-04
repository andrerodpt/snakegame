from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        x_pos = 0
        y_pos = 0
        for _ in range(3):
            t = Turtle(shape='square')
            t.penup()
            t.speed('fastest')
            t.color('white')
            t.goto(x_pos, y_pos)
            x_pos -= 20
            self.snake_body.append(t)


    def reset(self):
        for body_part in self.snake_body:
            body_part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def move(self):
        for body_part in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[body_part-1].xcor()
            new_y = self.snake_body[body_part-1].ycor()
            self.snake_body[body_part].goto(new_x, new_y)
        self.head.forward(20)

    
    def setheading(self, heading):
        opposite_heading = heading + 180
        if opposite_heading >= 360:
            opposite_heading -= 360 
        if self.head.heading() != opposite_heading:
            self.head.setheading(heading)
    

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)

    def right(self):
        self.setheading(0)
    
    def left(self):
        self.setheading(180)


    def add_segment(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.setpos(self.snake_body[-1].position())
        self.snake_body.append(new_segment)


    def extend(self):
        self.add_segment()