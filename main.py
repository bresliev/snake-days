from turtle import Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sssssssssssssnake")
screen.tracer(0)
screen.listen()


snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) >= 15:
        pass
    #detect colision
    else:
        food.refresh()
        score.increase_score()
        snake.extend()

    #detect colision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect colision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.game_over()

screen.exitonclick()
