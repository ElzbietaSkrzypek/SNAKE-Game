from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

speed = 0.08
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    scoreboard.score()


# Detect collision with food
    if snake.full_snake[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.score()
        speed *= 0.9


# Detect collision with wall.
    if snake.full_snake[1].xcor() > 280 or snake.full_snake[1].xcor() < - 280 or snake.full_snake[1].ycor() > 280 or \
            snake.full_snake[1].ycor() < - 280:
            scoreboard.reset()
            snake.reset()
            speed = 0.08

# Detect collision with tail.
# If head collides with any segment in the tail:
# trigger game over

    for segments in snake.full_snake[1:]:
        if snake.full_snake[0].distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
            speed = 0.08


screen.exitonclick()
