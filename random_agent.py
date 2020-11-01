from logic2048 import Game2048

def main():
    game = Game2048()

    for row in game.matrix:
        print(row)

    while not game.game_end:
        move = input("Move: ")
        if move == "w":
            game.move_up()        
        if move == "s":
            game.move_down()
        if move == 'a':
            game.move_left()
        if move == 'd':
            game.move_right()

        for row in game.matrix:
                print(row)
    

if __name__ == '__main__':
    main()