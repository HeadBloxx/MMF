def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()