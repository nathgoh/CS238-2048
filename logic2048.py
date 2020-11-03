import random
import copy

class Game2048():
    def __init__(self):
        self.matrix = [[0,0,0,0] for i in range(4)]
        self.matrix[random.randint(0, 3)][random.randint(0, 3)] = random.choice([2, 4])
        self.game_end = False
        self.merge_score = 0

    def __str__(self):
        output = ""
        for row in self.matrix:
            output += str(row) + "\n"
        return output

    def check_game(self):
        # If there is at least one empty square
        self.game_end = not (0 in self.matrix[0] or 0 in self.matrix[1] or 0 in self.matrix[2] or 0 in self.matrix[3])
        
        # If no empty square but you can still merge
        if self.game_end:
            for j in range(3): 
                for k in range(3): 
                    if(self.matrix[j][k] == self.matrix[j + 1][k] or self.matrix[j][k] == self.matrix[j][k + 1]): 
                        self.game_end = False

            for j in range(3): 
                if(self.matrix[3][j] == self.matrix[3][j + 1]): 
                    self.game_end = False                

            for j in range(3): 
                if(self.matrix[j][3] == self.matrix[j + 1][3]):  
                    self.game_end = False
        
    def get_number(self):
        row, col = random.randint(0, 3), random.randint(0, 3)
        while self.matrix[row][col] != 0:
            row, col = random.randint(0, 3), random.randint(0, 3)
            
        self.matrix[row][col] = random.choice([2, 4])
        
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
        matrix_copy = copy.deepcopy(self.matrix)
        for col in range(len(self.matrix[0])):
            s = []
            for row in range(len(self.matrix)):
                if self.matrix[row][col] != 0:
                    s.append(self.matrix[row][col])
            i = 0
            while i < len(s) - 1:
                if s[i] == s[i+1]:
                    s[i] *= 2
                    self.merge_score += s[i]
                    s.pop(i+1)
                    i -= 1
                i += 1
            for row in range(len(self.matrix)):
                if len(s) > 0:
                    val = s.pop(0)
                    self.matrix[row][col] = val
                else:
                    self.matrix[row][col] = 0

        if matrix_copy != self.matrix:
            self.get_number()       
        self.check_game()

    def move_up(self):
        self.merge()

    def move_down(self):
        self.double_rotate()
        self.merge()
        self.double_rotate()

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

    def make_move(self, move):
        if move == 0:
            self.move_up()        
        if move == 1:
            self.move_down()
        if move == 2:
            self.move_left()
        if move == 3:
            self.move_right()

    def get_sum(self):
        total_sum = 0
        for row in self.matrix:
            total_sum += sum(row)
        return total_sum

    def max_num(self):
        return max(map(max, self.matrix))

    def get_merge_score(self):
        return self.merge_score
