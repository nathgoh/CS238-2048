filename = "testing.txt"
with open(filename, 'r') as f:
    i = 0
    totalMax = 0
    totalSum = 0
    totalMerge = 0
    for line in f:
        line.strip()
        parts = line.split(":")
        if i%3 == 0:
            totalMax += int(parts[1])
        elif i%3 == 1:
            totalSum += int(parts[1])
        else: 
            totalMerge += int(parts[1])
        i+=1
    print("Num Trials:", i/3)
    print("Num Trials Left:", 100 - i/3)
    print("Avg Max:",totalMax // (i/3))
    print("Avg Total:", totalSum // (i/3))
    print("Avg Merge:", totalMerge // (i/3))