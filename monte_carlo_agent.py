from logic2048 import Game2048
import random, copy
import sys
import time
from datetime import timedelta

"""
montecarlo -- change line 15 for lookahead with rollouts 
    and use depth
using the sum of tiles
"""

NUM_ITERS = 100       
NUM_TRIALS = 100
EVAL_METHOD = 0

def random_run(game):
    game_copy = copy.deepcopy(game)
    while not game_copy.game_end: 
        move = random.randint(0, 3)
        game_copy.make_move(move)
    
    return game_copy.max_num(), game_copy.get_sum(), game_copy.get_merge_score()

def monte_carlo_iter(game):
    best_move = None
    best_total_sum = -1
    best_total_largest = -1
    best_total_merge = -1

    # For each move (0 - 3)
    for move in range(0,4):
        game_copy = copy.deepcopy(game)
        game_copy.make_move(move)
        if str(game_copy) == str(game):
            continue

        total_sum = 0
        total_largest = 0
        total_merge_score = 0

        # Try lots of paths with that move using random rollout policy
        for i in range(NUM_ITERS):
            output = random_run(game_copy)   # 0 for largest tile, 1 for sum
            total_largest += output[0] 
            total_sum += output[1]
            total_merge_score += output[2]

        # Eval Method 0: Best total sum
        if EVAL_METHOD == 0:
            if total_sum > best_total_sum:
                best_move = move
                best_total_sum = total_sum
        
        # Eval Method 1: Largest tile number, and best total sum
        elif EVAL_METHOD == 1:
            if total_largest > best_total_largest or (total_largest == best_total_largest and total_sum > best_total_sum):
                best_move = move
                best_total_largest = total_largest
                best_total_sum = total_sum
        
        # Eval Method 2: Largest total merge score
        elif EVAL_METHOD == 2:
            if total_merge_score > best_total_merge:
                best_move = move
                best_total_merge = total_merge_score

    game.make_move(best_move)
<<<<<<< HEAD
    print(game)
=======
    # print(game)
>>>>>>> main
    # print(game.max_num())
    # print(game.get_sum())
    # print(game.get_merge_score())
    # print("--------------------")

def monte_carlo_run():
    game = Game2048()
    while not game.game_end:
        monte_carlo_iter(game)

    print("Max Square Value: {}".format(game.max_num()))
    print("Total Square Sum: {}".format(game.get_sum()))
    print("Total Merge Score: {}".format(game.get_merge_score()))
    return game.max_num(), game.get_sum(), game.get_merge_score()

def main():
    if len(sys.argv) != 4:
        raise Exception("usage: python3 monte_carlo_agent.py <num_iters> <num_trials> <evaluation_method>")

    global NUM_ITERS 
    global NUM_TRIALS 
    global EVAL_METHOD
    NUM_ITERS = int(sys.argv[1])
    NUM_TRIALS = int(sys.argv[2])
    EVAL_METHOD = int(sys.argv[3])

    # Eval method 0: sum of all tiles
    # Eval method 1: largest tiles on board, then sum of all tiles if tied largest tile
    # Eval method 2: merge score
    if EVAL_METHOD < 0 or EVAL_METHOD > 2:
        raise Exception("Please choose an evaluation between 0-2")
    
    max_val_results = [0] * NUM_TRIALS
    total_sum_results = [0] * NUM_TRIALS
    total_merge_score = [0] * NUM_TRIALS
    
    start_time = time.time()
    for i in range(NUM_TRIALS):
        max_val_results[i], total_sum_results[i], total_merge_score[i] = monte_carlo_run()
    end_time = time.time()
        
    total_sum_avg = sum(total_sum_results) / NUM_TRIALS
    max_val_avg = sum(max_val_results) / NUM_TRIALS
    total_merge_avg = sum(total_merge_score) / NUM_TRIALS

    f = open("monte_carlo_" + str(NUM_ITERS) + "_" + str(NUM_TRIALS) + "_" + str(EVAL_METHOD) + ".txt", "w")
    f.write("avg max val: " + str(max_val_avg) + "\n") 
    f.write("avg total sum: " + str(total_sum_avg) + "\n")
    f.write("avg merge score: " + str(total_merge_avg) + "\n")
    f.write("max vals: " + str(max_val_results) + "\n") 
    f.write("total sums: " + str(total_sum_results) + "\n")
    f.write("total merge score: " + str(total_merge_score) + "\n")
    f.close()

    print("total sum avg: " + str(total_sum_avg))
    print("max val avg: " + str(max_val_avg))
    print("merge score avg: " + str(total_merge_avg))
    print()
    print("time taken: ", str(timedelta(seconds=(end_time - start_time))))

if __name__ == '__main__':
    main()
