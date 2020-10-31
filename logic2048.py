import random

class Game2048():
    def __init__(self):
        self.matrix = [[0,0,0,0] for i in range(4)]
        self.matrix[random.randint(0, 3)][random.randint(0, 3)] = random.choice([2, 4])
        self.game_end = False
        
    def get_number(self):
        self.game_end = not (0 in self.matrix[0] or 0 in self.matrix[1] or 0 in self.matrix[2] or 0 in self.matrix[3])
        while not self.game_end:
            row, col = random.randint(0, 3), random.randint(0, 3)
            if self.matrix[row][col] == 0:
                self.matrix[row][col] == random.choice([2, 4])
    
    def rotate(self):
        out = []
        for col in range(len(self.matrix[0])):
            temp = []
            for row in reversed(range(len(self.matrix[0]))):
                temp.append(self.matrix[row][col])
            out.append(temp)
        self.matrix = out

    def double_rotate(self):
        for j in range(2):
            self.rotate()

    def merge(self):
        for col in range(len(self.matrix[0])):
            s = []
            for row in range(len(self.matrix)):
                if self.matrix[row][col] != 0:
                    s.append(self.matrix[row][col])
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    s[i] *= 2
                    s.pop(i+1)
                    i-=1
                i+=1
            for row in range(len(self.matrix)):
                if len(s) > 0:
                    val = s.pop(0)
                    self.matrix[row][col] = val
                else:
                    self.matrix[row][col] = 0
        self.get_number()

    def move_up(self):
        self.merge()

    def move_down(self):
        self.double_rotate()
        self.merge()
        self.rotate()

    def move_right(self):
        self.double_rotate()
        self.rotate()
        self.merge()
        self.rotate()

    def move_left(self):
        self.rotate()
        self.merge()
        self.double_rotate()
        self.rotate()
