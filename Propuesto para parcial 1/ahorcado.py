class Ahorcado:
    
    
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.used_letters = []
        self.board = str(Board(len(self.secret_word)))
        self.lifes_left = 6
        self.is_over = False
        self.win = False
        
    def new_letter(self, letter):
        if letter not in self.used_letters:
            self.used_letters.append(letter)
                
    def change(self,letter):
        print([ i*2 for i, c in enumerate(self.secret_word) if c == letter])
        if letter not in self.used_letters and letter in self.secret_word:
            for i in [i*2 for i, c in enumerate(self.secret_word) if c == letter]:
                print(self.board)

                self.board = self.board[:i] + letter + self.board[i+1:]
            
    def lose_life(self, letter):
        if letter not in self.secret_word and letter not in self.used_letters and self.lifes_left != 0:
            print(self.lifes_left)
            self.lifes_left -= 1
  
    def play(self, letter):
        #while self.is_over == False:
        if not self.is_over:
            print(self)
            #new_letter = str(input('Letra:'))
            self.change(letter)
            self.lose_life(letter)
            self.new_letter(letter)
            print(self.lifes_left)
            print(self.used_letters)
            print(self.board)
            if self.secret_word == self.board.replace(' ', ''):
                print('YOU WIN!!!')
                self.win = True
                self.is_over = True
            if self.lifes_left == 0:
                print('YOU LOSE :(')
                self.is_over = True
               

class Board:
    def __init__(self,leng):
        self.leng = leng
        self.letters = []
              
    def __str__ (self):
        for i in range(self.leng):
            self.letters.append('_')
        return " ".join(self.letters)
                 
    
if __name__ == '__main__':
    game = Ahorcado('PERRO')
    game.play('A')
    game.play('R')
    game.play('R')
    game.play('E')
    game.play('Z')
    game.play('Q')
    game.play('T')
    game.play('L')
    game.play('P')
    game.play('O')
    game.play('Q')
    game.play('Y')
