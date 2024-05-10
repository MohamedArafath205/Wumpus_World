import random

class Wumpus_world():
    
    def __init__ (self):
        
        self.game_over = False
        self.player_move = ""
        self.points = 0
        self.player_pos_x = 14
        self.player_pos_y = 4
        
        self.defboard = [
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   ?   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   ?   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   ?   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   →   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66]
        ]
        
        self.env_board = [
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   ?   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   ?   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   ?   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66],
            list("|       |       |       |       |"),
            list("|   →   |   ?   |   ?   |   ?   |"),
            list("|       |       |       |       |"),
            ["-" * 66]
        ]
        
        self.x_choice = [2, 6, 10, 14]
        self.y_choice = [4, 12, 20, 28]
    
    def default_board(self):
        self.reshaped_array = [ self.defboard[i:i+1] for i in range(0,17) ]
        for row in self.reshaped_array:
            for line in row:
                print(*line)
            
    
    def player_board(self):
        self.reshaped_array = [ self.env_board[i:i+1] for i in range(0,17) ]
        for row in self.reshaped_array:
            for line in row:
                print(*line)
    
    def set_wumpus(self):
        x = random.choice(self.x_choice)
        y = random.choice(self.y_choice)
        if (x == 14 and y == 4):
            x = random.choice(self.x_choice)
            y = random.choice(self.y_choice)
            
        else:
            if(self.env_board[x][y] == "?"):
                self.env_board[x][y] = "W"
                self.x_choice.remove(x)
                self.y_choice.remove(y)
                
        return self.env_board
                
    def set_pit(self):
        for i in range(2):
            x = random.choice(self.x_choice)
            y = random.choice(self.y_choice)
            if (x == 14 and y == 4):
                x = random.choice(self.x_choice)
                y = random.choice(self.y_choice)
            
            else:
                if(self.env_board[x][y] != "W"):
                    if(self.env_board[x][y] == "?"):
                        self.env_board[x][y] = "P"
                        self.x_choice.remove(x)
                        self.y_choice.remove(y)
        
        return self.env_board
    
    def env_hint(self):
        for i in [2, 6, 10, 14]:
            for j in [4, 12, 20, 28]:
                if self.env_board[i][j] == "W":   
                    if j - 11 >= 0:
                        self.env_board[i-1][j - 11] = "S"
                    if j + 5 < len(self.env_board[i]):
                        self.env_board[i-1][j + 5] = "S"
                    if i - 5 >= 0 and j - 3 >= 0:
                        self.env_board[i - 5][j - 3] = "S"
                    if i + 3 < len(self.env_board) and j - 3 >= 0:
                        self.env_board[i + 3][j - 3] = "S"
                    
                if self.env_board[i][j] == "P":
                    if j - 10 >= 0:
                        self.env_board[i-1][j - 10] = "B"
                    if j + 6< len(self.env_board[i]):
                        self.env_board[i-1][j + 6] = "B"
                    if i - 5 >= 0 and j - 2 >= 0:
                        self.env_board[i - 5][j - 2] = "B"
                    if i + 3 < len(self.env_board) and j - 2 >= 0:
                        self.env_board[i + 3][j - 2] = "B"
                        
        return self.env_board
    
    def gold_func(self):
        x_gold = random.choice(self.x_choice)
        y_gold = random.choice(self.y_choice)
        if (x_gold == 14 and y_gold == 4):
            x_gold = random.choice(self.x_choice)
            y_gold = random.choice(self.y_choice)
            
        else:
            self.env_board[x_gold-1][y_gold-1] = "G"
            self.x_choice.remove(x_gold)
            self.y_choice.remove(y_gold)
        
        return self.env_board
    
    def start(self):
        self.set_wumpus()
        self.set_pit()
        self.env_hint()
        self.gold_func()
        
        if(self.env_board[self.player_pos_x-1][self.player_pos_y-2] == "B"):
            self.defboard[self.player_pos_x-1][self.player_pos_y-2] = self.env_board[self.player_pos_x-1][self.player_pos_y-2]
                
        if(self.env_board[self.player_pos_x-1][self.player_pos_y-3] == "S"):
            self.defboard[self.player_pos_x-1][self.player_pos_y-3] = self.env_board[self.player_pos_x-1][self.player_pos_y-3]
        
        self.default_board()
        
        while not self.game_over:
            
            print("'l' for left, 'r' for right, 'u' for up, 'd' for down, 'g' for grab")
            print("Enter your move: ")
            self.player_move = input()
            if(self.player_move == "l"):
                self.defboard[self.player_pos_x][self.player_pos_y] = "←"
            if(self.player_move == "r"):
                self.defboard[self.player_pos_x][self.player_pos_y] = "→"
            if(self.player_move == "u"):
                self.defboard[self.player_pos_x][self.player_pos_y] = "↑"
            if(self.player_move == "d"):
                self.defboard[self.player_pos_x][self.player_pos_y] = "↓"
                
            if(self.player_move == "f"):
                
                if(self.defboard[self.player_pos_x][self.player_pos_y] == "←" and self.player_pos_y - 8 >= 0):
                    self.defboard[self.player_pos_x][self.player_pos_y] = " "
                    self.player_pos_y -= 8
                    self.defboard[self.player_pos_x][self.player_pos_y] = "←"
                    
                if(self.defboard[self.player_pos_x][self.player_pos_y] == "→" and self.player_pos_y + 8 < len(self.defboard[self.player_pos_x])):
                    self.defboard[self.player_pos_x][self.player_pos_y] = " "
                    self.player_pos_y += 8
                    self.defboard[self.player_pos_x][self.player_pos_y] = "→"
                    
                if(self.defboard[self.player_pos_x][self.player_pos_y] == "↑" and self.player_pos_x - 4 >= 0):
                    self.defboard[self.player_pos_x][self.player_pos_y] = " "
                    self.player_pos_x -= 4
                    self.defboard[self.player_pos_x][self.player_pos_y] = "↑"
                    
                if(self.defboard[self.player_pos_x][self.player_pos_y] == "↓" and self.player_pos_x + 4 < len(self.defboard)):
                    self.defboard[self.player_pos_x][self.player_pos_y] = " "
                    self.player_pos_x += 4
                    self.defboard[self.player_pos_x][self.player_pos_y] = "↓"
                    
                if(self.env_board[self.player_pos_x-1][self.player_pos_y-2] == "B"):
                    self.defboard[self.player_pos_x-1][self.player_pos_y-2] = self.env_board[self.player_pos_x-1][self.player_pos_y-2]
                
                if(self.env_board[self.player_pos_x-1][self.player_pos_y-3] == "S"):
                    self.defboard[self.player_pos_x-1][self.player_pos_y-3] = self.env_board[self.player_pos_x-1][self.player_pos_y-3]
                
                if(self.env_board[self.player_pos_x][self.player_pos_y] == "P" or self.env_board[self.player_pos_x][self.player_pos_y] == "W"):
                    print("You are dead")
                    self.game_over = True
                
            self.default_board()
            
                    
game = Wumpus_world()
game.start()
