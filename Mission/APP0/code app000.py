while NOT is_on_target():
    while get_direction() != EAST:
        turn_left():
            
    while get_X() != get_target_X():
        if get_X() =< get_target_X():
            while get_direction() != EAST:
                turn_left():
            if can_move():
                if is_in_front_of_wolf():
                    if get_y() =< get_target_y():
                        turn_right()
                        move()
                        turn_left()
                    else:
                        turn_left()
                        move()
                        turn_right()
                else:
                    move()
            else:
                turn_left()
                if can_move():
                    move()
                    turn_right()
                else:
                    turn_right
                    turn_right
                    move()
                    turn_left()
        else:
            while get_direction() != WEST:
                turn_left():
            if can_move():
                if is_in_front_of_wolf():
                    if get_y() =< get_target_y():
                        turn_right()
                        move()
                        turn_left()
                    else:
                        turn_left()
                        move()
                        turn_right()
                else:
                    move()
            else:
                turn_left()
                if can_move():
                    move()
                    turn_right()
                else:
                    turn_right()
                    turn_right()
                    move()
                    turn_left()

    while get_Y() != get_target_Y():
        if get_Y() =< get_target_Y():
            turn_right()
            while not is_on_target():
                if can_move():
                    if is_on_front_of_wolf():
                        turn_right()
                        move()
                        turn_left()
                        move()
                        move()
                        turn_left()
                        move() 
                        turn_right()
                    else:
                        move()
                else:
                    turn_right()
                    if can_move():
                        move()
                        turn_left()
                    else:
                        turn_left()
                        move()
                        turn_right()
                        
        else:
            turn_left()
            while not is_on_target():
                    if can_move():
                        if is_on_front_of_wolf():
                            turn_left()
                            move()
                            turn_right()
                            move()
                            move()
                            turn_right()
                            move()
                            turn_left()
                        else:
                            move()
                    else:
                        turn_left()
                        if can_move():
                            move()
                            turn_right()A
                        else:
                            turn_right()
                            turn_right()
                            move()
                            turn_left()
spy_on_target():
 