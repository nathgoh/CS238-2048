from logic2048 import Game2048
import random

def random_run():
    game = Game2048()

    print(game)
    
    while not game.game_end:
        move = random.randint(0, 3)
        game.make_move(move)
        print(game)
        
    print("Max Square Value: {}".format(game.max_num()))
    print("Total Square Sum: {}".format(game.get_sum()))
    return game.max_num(), game.get_sum()

def main():
    max_val_results = [0] * 1000
    total_sum_results = [0] * 1000
    
    for i in range(1000):
        max_val_results[i], total_sum_results[i] = random_run()
        
    total_sum_avg = sum(total_sum_results) / 1000
    max_val_avg = sum(max_val_results) / 1000

    f = open("random.txt", "w")
    f.write("avg max val: " + str(max_val_avg) + "\n") 
    f.write("avg total sum: " + str(total_sum_avg)+ "\n")
    f.write("max vals: " + str(max_val_results)+ "\n") 
    f.write("total sums: " + str(total_sum_results)+ "\n")
    f.close()

    print("total sum avg: " + str(total_sum_avg))
    print("max val avg: " + str(max_val_avg))

if __name__ == '__main__':
    main()