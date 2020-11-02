from logic2048 import Game2048
import random, copy

"""
montecarlo -- change line 15 for lookahead with rollouts 
    and use depth
using the sum of tiles
"""

DEPTH = 10             
NUM_ITERS = 100         

def random_run(game, starting_move):
    game_copy = copy.deepcopy(game)
    game_copy.make_move(starting_move)
    while not game.game_end: 
        if game_copy.game_end:
            break
        move = random.randint(0, 3)
        game_copy.make_move(move)
    return game_copy.max_num(), game_copy.get_sum() 

def monte_carlo_iter(game):
    best_move = None
    best_total_sum = -1

    # For each move (0 - 3)
    for i in range(0,4):
        total_sum = 0

        # Try lots of paths with that move using random rollout policy
        for j in range(NUM_ITERS):
            total_sum += random_run(game, i)[1]
        if total_sum > best_total_sum:
            best_move = i
            best_total_sum = total_sum
    game.make_move(best_move)

    for row in game.matrix:
        print(row)
    print()

def monte_carlo_run():
    game = Game2048()
    while not game.game_end:
        monte_carlo_iter(game)
    print("Max Square Value: {}".format(game.max_num()))
    print("Total Square Sum: {}".format(game.get_sum()))
    return game.max_num(), game.get_sum() 

def main():
    max_val_results = [0] * NUM_TRIALS
    total_sum_results = [0] * NUM_TRIALS
    
    for i in range(100):
        max_val_results[i], total_sum_results[i] = monte_carlo_run()
        
    total_sum_avg = sum(total_sum_results) / NUM_TRIALS
    max_val_avg = sum(max_val_results) / NUM_TRIALS

    f = open("monte_carlo_" + str(DEPTH) + "_" + str(NUM_ITERS) + ".txt", "w")
    f.write("avg max val: " + str(max_val_avg)) 
    f.write("avg total sum: " + str(total_sum_avg))
    f.write("max vals: " + str(max_val_results)) 
    f.write("total sums: " + str(total_sum_results))
    f.close()

    print("total sum avg: " + str(total_sum_avg))
    print("max val avg: " + str(max_val_avg))

if __name__ == '__main__':
    main()
