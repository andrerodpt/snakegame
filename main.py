from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

level = 0.2

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

print(scoreboard.pos())
print(scoreboard.color())

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(level)
    snake.move()

    ## Detect collision with food
    if snake.head.distance(food) < 15:
        ## Add 1 to the score
        scoreboard.increment_score()
        ## Add a segment to the snake
        snake.extend()
        ## Generate a new location for the food
        food.refresh()

    ## Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False 
        scoreboard.game_over()

    ## Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()



















screen.exitonclick()