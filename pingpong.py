import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("The Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Function to ask for the player names within the turtle window
def ask_for_player_names():
    player1_name = wn.textinput("Enter Player 1's Name", "Enter the name of Player 1:")
    player2_name = wn.textinput("Enter Player 2's Name", "Enter the name of Player 2:")
    return player1_name, player2_name

# Function to ask for the game mode (2-player or vs AI) within the turtle window
def ask_for_game_mode():
    return wn.textinput("Game Mode", "Enter '1' for 2-Player mode or '2' to play against 'The Unbeatable AI': ")

# Ask for game mode and player names
game_mode = ask_for_game_mode()
player1_name, player2_name = ask_for_player_names()

# Variable for the pause state
paused = False

# Pen for Paused message
paused_pen = turtle.Turtle()
paused_pen.speed(0)
paused_pen.color("white")
paused_pen.penup()
paused_pen.hideturtle()
paused_pen.goto(0, 0)

# Toggle pause state
def toggle_pause():
    global paused
    paused = not paused
    if paused:
        paused_pen.goto(0, 0)
        paused_pen.write(" PAUSED ", align="center", font=("Courier", 32, "normal"))
    else:
        paused_pen.clear()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0.75)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3.0
ball.dy = 3.5  # Actually increases the speed

# Pen for scores
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write(f"{player1_name}: 0 {player2_name}: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Function to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Simple AI for paddle B
def ai_move():
    if ball.ycor() > paddle_b.ycor():
        paddle_b_up()
    elif ball.ycor() < paddle_b.ycor():
        paddle_b_down()

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(toggle_pause, "space")

# Main Game Loop
while True:
    wn.update()

    if not paused: 
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            score_pen.clear()
            score_pen.write(f"{player1_name}: {score_a} {player2_name}: {score_b}", align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            score_pen.clear()
            score_pen.write(f"{player1_name}: {score_a} {player2_name}: {score_b}", align="center", font=("Courier", 24, "normal"))

        # Paddle and Ball Collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

        # Paddle Borders
        if paddle_a.ycor() > 290:
            paddle_a.sety(290)

        if paddle_a.ycor() < -290:
            paddle_a.sety(-290)

        # Check game mode and move paddle B accordingly
        if game_mode == '1':
            # 2-Player Mode: Allow player 2 to move paddle_b
            wn.listen()
            wn.onkeypress(paddle_b_up, "Up")
            wn.onkeypress(paddle_b_down, "Down")
        elif game_mode == '2':
            # AI Mode: Move paddle_b automatically
            ai_move()

        if paddle_b.ycor() > 290:
            paddle_b.sety(290)

        if paddle_b.ycor() < -290:
            paddle_b.sety(-290)

# Keep the window open
turtle.mainloop()
