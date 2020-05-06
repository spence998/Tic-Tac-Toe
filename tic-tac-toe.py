import pygame
import sys
from random import randint
from random import seed
import time
seed()
pygame.init()

#Screen
width = 600
height = 600
screen = pygame.display.set_mode((width,height))
win_lose_game = False
white = (255,255,255)
black = (0,0,0)
turn = 1
X_win = False
O_win = False
menu_end = False
one_p_flag = False
two_p_flag = False
colour_left = (252,3,252)
colour_right = (252,252,3)

letterX = pygame.image.load('crosses.png')
letterO = pygame.image.load('naught.png')
matrix = ['.','.','.','.','.','.','.','.','.']

#Function for creating a message in the middle of the screen
font = pygame.font.SysFont('snapitc',23)
font2 = pygame.font.SysFont('arial',23)
def message(msg,msgcolour,x,y):
	screen_text = font.render(msg,True,msgcolour)
	screen.blit(screen_text, [x,y])
def message2(msg,msgcolour,x,y):
	screen_text = font2.render(msg,True,msgcolour)
	screen.blit(screen_text, [x,y])

def screen_fill():
	screen.fill(white)
	pygame.draw.line(screen,black,(0,height/3),(width,height/3),4)
	pygame.draw.line(screen,black,(0,2*height/3),(width,2*height/3),4)
	pygame.draw.line(screen,black,(width/3,0),(width/3,height),4)
	pygame.draw.line(screen,black,(2*width/3,0),(2*width/3,height),4)

	for i in range(9):
		if matrix[i] == "X":
			if i < 3:
				screen.blit(letterX,(i*200,0))
			if i < 6 and i > 2:
				screen.blit(letterX,((i-3)*200,200))
			if i > 5:
				screen.blit(letterX,((i-6)*200,400))
		elif matrix[i] == "O":
			if i < 4:
				screen.blit(letterO,(i*200+10,0-5))
			if i < 6 and i > 2:
				screen.blit(letterO,((i-3)*200+10,200-5))
			if i > 5:
				screen.blit(letterO,((i-6)*200+10,400-5))

def game_play():
	global mouse_click_pos 
	global turn
	k = 0

	for i in range(3):
		for j in range(3):
			if  mouse_click_pos[1] > 200*(i) and mouse_click_pos[1] < 200*(i+1) and mouse_click_pos[0] > 200*(j) and mouse_click_pos[0] < 200*(j+1) and matrix[k] == '.':
				XorO = turn % 2
				if XorO == 1:
					matrix[k] = "X"
				if XorO == 0:
					matrix[k] = "O"
				turn = turn + 1	
			k=k+1

def game_play_one_player():
	global mouse_click_pos 
	global turn
	
	if (turn % 2) == 0 and turn < 10:
		best_score = -99999
		for i in range(9):
			if matrix[i] == ".":
				matrix[i] = "O"
				score = minimax(matrix,False)	
				matrix[i] = "."
				if score > best_score:
					best_score = score
					move = i
					
		matrix[move] = "O"
		turn = turn + 1
	
	k = 0
	if (turn % 2) == 1:
		for i in range(3):
			for j in range(3):
				if  mouse_click_pos[1] > 200*(i) and mouse_click_pos[1] < 200*(i+1) and mouse_click_pos[0] > 200*(j) and mouse_click_pos[0] < 200*(j+1) and matrix[k] == '.':
					matrix[k] = "X"
					turn = turn + 1	
				k = k + 1

def minimax(board,O_turn):
	global X_win, O_win
	check_win_condition(board)
	if X_win == True:
		X_win = False
		return -10
	elif O_win == True:
		O_win = False
		return +10
	else:
		draw_counter = True
		for i in range(9):
			if (matrix[i] == "."):
				draw_counter = False
		if draw_counter == True:
			return 0
			
	if O_turn:
		best_score = -99999
		for i in range(9):
			if board[i] == ".":
				board[i] = "O"
				score = minimax(board,False)
				board[i] = "."
				best_score = max(score,best_score)
			if best_score == 10:
				break
		return best_score
	else:
		best_score = 99999
		for i in range(9):
			if board[i] == ".":
				board[i] = "X"
				score = minimax(board,True)
				board[i] = "."
				best_score = min(score,best_score)
			if best_score == -10:
				break
		return best_score


def check_win_condition(matrix):
	global X_win,O_win
	X_win = False
	O_win = False
	#X winning conditions
	#horizontal
	if matrix[0] == 'X' and matrix[1] == 'X' and matrix[2] == 'X':
		X_win = True
	if matrix[3] == 'X' and matrix[4] == 'X' and matrix[5] == 'X':
		X_win = True
	if matrix[6] == 'X' and matrix[7] == 'X' and matrix[8] == 'X':
		X_win = True
	#verticle
	if matrix[0] == 'X' and matrix[3] == 'X' and matrix[6] == 'X':
		X_win = True
	if matrix[1] == 'X' and matrix[4] == 'X' and matrix[7] == 'X':
		X_win = True
	if matrix[2] == 'X' and matrix[5] == 'X' and matrix[8] == 'X':
		X_win = True
	#diagonal
	if matrix[0] == 'X' and matrix[4] == 'X' and matrix[8] == 'X':
		X_win = True
	if matrix[6] == 'X' and matrix[4] == 'X' and matrix[2] == 'X':
		X_win = True

	#O winning conditions
	#horizontal
	if matrix[0] == 'O' and matrix[1] == 'O' and matrix[2] == 'O':
		O_win = True
	if matrix[3] == 'O' and matrix[4] == 'O' and matrix[5] == 'O':
		O_win = True
	if matrix[6] == 'O' and matrix[7] == 'O' and matrix[8] == 'O':
		O_win = True
	#verticle
	if matrix[0] == 'O' and matrix[3] == 'O' and matrix[6] == 'O':
		O_win = True
	if matrix[1] == 'O' and matrix[4] == 'O' and matrix[7] == 'O':
		O_win = True
	if matrix[2] == 'O' and matrix[5] == 'O' and matrix[8] == 'O':
		O_win = True
	#diagonal
	if matrix[0] == 'O' and matrix[4] == 'O' and matrix[8] == 'O':
		O_win = True
	if matrix[6] == 'O' and matrix[4] == 'O' and matrix[2] == 'O':
		O_win = True

def win_screen():
	if X_win == True:
		screen.fill(white)
		message("X wins!",black,width/2 - 30,height/2)
		one_p_flag = False
		two_p_flag = False
	elif O_win == True:
		screen.fill(white)
		message("O wins!",black,width/2 - 30,height/2)
		one_p_flag = False
		two_p_flag = False
	elif turn == 10:
		screen.fill(white)
		message("Draw!",black,width/2 - 30,height/2)
		one_p_flag = False
		two_p_flag = False

def start_menu_screen():
	global mouse_pos, menu_end,one_p_flag,two_p_flag
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	pygame.draw.rect(screen,colour_left,[(0,0),(300,600)])
	pygame.draw.rect(screen,colour_right,[(300,0),(300,600)])
	message("Which type of game would you like to play?",black,width/4 - 130,height/2 - 40)		
	if mouse_pos[0] < 300:
		message("1-player",black,width/4 - 40,height/2)
		message2("2-player",black,3*width/4 - 40,height/2)
	if mouse_pos[0] > 300:
		message2("1-player",black,width/4 - 40,height/2)
		message("2-player",black,3*width/4 - 40,height/2)
	if pygame.mouse.get_pressed() == (1,0,0):
		mouse_click_pos = pygame.mouse.get_pos()
		if mouse_click_pos[0] < 300:
			menu_end = True
			one_p_flag = True
		if mouse_click_pos[0] > 300:
			menu_end = True
			two_p_flag = True
	pygame.display.update()

while not win_lose_game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	#This is going to be the part where it decides if it is going to be 1p or 2p
	while menu_end == False:
		pygame.font.get_fonts()
		mouse_pos = pygame.mouse.get_pos()
		start_menu_screen()
	#main game	
	screen_fill()
	if two_p_flag == True:		
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed() == (1,0,0):
				mouse_click_pos = pygame.mouse.get_pos()
				game_play()
	if one_p_flag == True:
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed() == (1,0,0):
				mouse_click_pos = pygame.mouse.get_pos()
				game_play_one_player()
	check_win_condition(matrix)	
	win_screen()
	pygame.display.update()
