from logic2048 import Game2048
import random

def main():
    game = Game2048()

    for row in game.matrix:
        print(row)
    print()

    while not game.game_end:
        move = random.randint(0, 3)
        if move == 0:
            game.move_up()        
        if move == 1:
            game.move_down()
        if move == 2:
            game.move_left()
        if move == 3:
            game.move_right()

        for row in game.matrix:
                print(row)
        print()
        
    print("Max Square Value: {}".format(max(max(game.matrix))))

if __name__ == '__main__':
    main()