import statistics
filename = "monte_carlo_50_100_0.txt"
with open(filename, 'r') as f:
    f.readline()
    f.readline()
    f.readline()

    max_vals = f.readline()
    total_sums = f.readline()
    merge_scores = f.readline()

    max_vals = max_vals.split(":")[1]
    max_vals = max_vals[2:-2]
    max_vals = max_vals.split(",")
    max_vals = [int(elem) for elem in max_vals]

    count_2048 = 0
    for i in max_vals:
        if i >= 2048:
            count_2048 += 1
    print(count_2048)

    merge_scores = merge_scores.split(":")[1]
    merge_scores = merge_scores[2:-2]
    merge_scores = merge_scores.split(",")
    merge_scores = [int(elem) for elem in merge_scores]
    print(statistics.stdev(merge_scores))




