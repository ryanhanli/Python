import random
import string

board_size = 10

words = input("Enter words separated by spaces: ").split()

#Generate the board
board = [['*' for _ in range(board_size)] for _ in range(board_size)]

#Print Grid/Board Function
def print_board():
    for x in range(board_size):
        print('\t'*4+' '.join(board[x]))
        
placements = ['horizontal','vertical']

for word in words:
    word_length = len(word)
    
    placed = False
    while not placed:
        placement = random.choice(placements)
        if placement == 'horizontal':
            step_x = 1
            step_y = 0
        if placement == 'vertical':
            step_x = 0
            step_y = 1
        
		#Generate random starting location for word
        x_position = random.randint(0,board_size)
        y_position = random.randint(0,board_size)
        
        ending_x = x_position + word_length*step_x
        ending_y = y_position + word_length*step_y
        
		#Check if word will fit on the board starting at the random position
        if ending_x<0 or ending_x>= board_size: continue
        if ending_y<0 or ending_y>= board_size: continue
    
        failed = False
        
		#Try placing the word if you run into an already placed character instead of star try again
        for i in range(word_length):
            character = word[i]
            
            new_position_x = x_position + i*step_x
            new_position_y = y_position + i*step_y
            
            character_at_new_position = board[new_position_x][new_position_y]
            if character_at_new_position != '*':
                if character_at_new_position == character:
                    continue
                else:
                    failed = True
                    break
            
        if failed:
            continue
		#Place the word onto the grid
        else:
            for i in range(word_length):
                character = word[i]
                
                new_position_x = x_position + i*step_x
                new_position_y = y_position + i*step_y
                
                board[new_position_x][new_position_y] = character
            placed = True
#Showcase the answers            
print("Board before:")
print_board()			

for x in range(board_size):
    for y in range(board_size):
        if (board[x][y]=='*'):
            board[x][y]=random.choice(string.ascii_uppercase)

print("Final board:")
print_board()