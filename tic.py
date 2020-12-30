#!/usr/bin/python3

from copy import deepcopy
from numpy import argmax, argmin

def idx2(data2, idx):
    return data2[idx[0]][idx[1]]

def turns(board):
    return sum([1 if cell != 0 else 0 for row in board for cell in row])

def iswinloss(board, me):
    them = 2 if me == 1 else 1
    trips = []
    trips += [[[0,0], [0,1], [0,2]]]
    trips += [[[1,0], [1,1], [1,2]]]
    trips += [[[2,0], [2,1], [2,2]]]
    trips += [[[0,0], [1,1], [2,2]]]
    trips += [[[0,2], [1,1], [2,0]]]
    trips += [[[0,0], [1,0], [2,0]]]
    trips += [[[0,1], [1,1], [2,1]]]
    trips += [[[0,2], [1,2], [2,2]]]
    for trip in trips:
        if idx2(board,trip[0]) == me and idx2(board,trip[1]) == me and idx2(board,trip[2]) == me:
            return 1
        if idx2(board,trip[0]) == them and idx2(board,trip[1]) == them and idx2(board,trip[2]) == them:
            return -1
    return 0

def minimax(board, me, turn, style):
    winloss = style*iswinloss(board, me)
    if winloss != 0:
        return winloss/turns(board), 0
    outcomes = []
    moves = []
    
    full = True
    next_turn = 2 if turn == 1 else 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                full = False
                next_board = deepcopy(board)
                next_board[i][j] = turn
                outcome, move = minimax(next_board, me, next_turn, style)
                outcomes += [outcome]
                moves += [[i,j]]

    if full:
        return 0,0
    
    if me == turn:
        idx = argmax(outcomes)
    else:
        idx = argmin(outcomes)
    return outcomes[idx], moves[idx]


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            cell = board[i][j]
            if cell == 0:
                print(i*3+j,end='')
            elif cell == 1:
                print('X',end='')
            else:
                print("O",end='')
            if j != 2:
                print('|',end='')
            else:
                print()
        if i != 2:
            print('-----')
    print()

board = [[0 for i in range(3)] for j in range(3)]
print_board(board)
style = int(input("Normal (1) or Misere (-1): "))
turn = 1
for i in range(9):
    if turn == 2:
        outcome, move = minimax(board,turn,turn,style)
    else:
        move_int = int(input("Move (0-8): "))
        move = divmod(move_int, 3)
    if move == 0:
        exit()
    board[move[0]][move[1]] = turn
    print_board(board)
    turn = 2 if turn == 1 else 1

