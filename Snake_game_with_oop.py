import random
import turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGN = 'center'
FONT = ('courier', 24, 'normal')


class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for i in range(3):
            self.add_seg_ment((-20*i, 0))

    def add_seg_ment(self, position):
        t = turtle.Turtle(shape='square')
        t.color('white')
        t.up()
        t.setposition(position)
        self.segments.append(t)

    def extend(self):
        self.add_seg_ment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_new = self.segments[seg - 1].xcor()
            y_new = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_new, y_new)
        self.head.fd(MOVE_DISTANCE)

    def up_ward(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down_ward(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]


colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(colors))
        self.speed(0)
        self.refresh()

    def refresh(self):

        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.color(random.choice(colors))
        self.goto(x_cord, y_cord)


class Score_Board(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('highest_score.txt', 'r') as hs:
            self.high_score = int(hs.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f'SCORE:{self.score} High score: {self.high_score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    # def Game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('highest_score.txt', 'w') as hs:
                hs.write(f'{self.high_score}')
        self.score = 0
        self.update_score()
