import turtle
import time
from Snake_game_with_oop import Snake, Food, Score_Board
s = turtle.Screen()
turtle.bgcolor('black')
s.title("MY SNAKE GAME")
s.tracer(0)
snake = Snake()
food = Food()
Score = Score_Board()

s.listen()
s.onkey(key='Up', fun=snake.up_ward)
s.onkey(key='Down', fun=snake.down_ward)
s.onkey(key='Left', fun=snake.left)
s.onkey(key='Right', fun=snake.right)

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        Score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 360 or snake.head.xcor() < -380 or snake.head.ycor() > 320 or snake.head.ycor() < -320:
        # is_game_on = False
        # Score.Game_over()
        Score.reset()
        snake.reset()

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            # Score.Game_over()
            Score.reset()
            snake.reset()

s.exitonclick()
