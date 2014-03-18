#!/usr/bin/env python3

import random
import collections
import sys
import os

GUESS_SIZE = 4
NUM_COLORS = 6
MAX_GUESSES = 12

NUM_COLOR_MAP = {0: 'Y', 
                 1: 'B', 
                 2: 'W', 
                 3: 'P', 
                 4: 'G', 
                 5: 'R'}
assert(len(NUM_COLOR_MAP) <= NUM_COLORS)

COLOR_NUM_MAP = { color: num for (num, color) in NUM_COLOR_MAP.items()}

PEGS = ['-', 'w', 'b']

def generate_target(guess_size=4, num_color=6):
    target = []
    for guess in range(guess_size):
        color = random.randint(0, num_color-1)
        target.append(color)
    
    return target

def score_guess(guess, target):
    assert len(guess) == len(target)
    score = [0] * len(guess)
    target_map = collections.Counter(target) 
    for index, color in enumerate(guess):
        if target[index] == color:
            target_map[color] -= 1
            score[index] = 2

    for index, color in enumerate(guess):
        if target_map[color] > 0 and score[index] != 2:
            target_map[color] -= 1
            score[index] = 1
    
    score.sort(reverse=True)
    return score

def draw_board(board):
    """ draws board that's a list of tuples containing guess and score.
        ex. board = [(guess, score), (guess, score)] 
            board = [([0, 0, 2, 5], [2,2,1,0])]

             r r b y | b b w - 
    """
    to_print = ""
    for guess, score in board:
        guess_string = ' '.join([NUM_COLOR_MAP[i] for i in guess])
        score_string = ' '.join([PEGS[i] for i in score])
        to_print += guess_string +  '  |  ' +  score_string + '\n'    
    
    print(to_print)
    return to_print

def is_valid_input(s):
    colors = s.split(' ')
    colors = [c.upper() for c in colors]
    if len(colors) != GUESS_SIZE:
        return False
    allowed_colors = list(COLOR_NUM_MAP.keys())[:NUM_COLORS]
    for c in colors:
        if c not in allowed_colors: 
            return False
    return True

def main():
    t = generate_target()
    b = []
    for _ in range(MAX_GUESSES):
        draw_board(b)
        while True:
            s = input("Please guess a sequence of colors from {0}: "\
                       .format(' '.join(list(COLOR_NUM_MAP.keys())[:NUM_COLORS])))
            if 'q' in s:
                sys.exit(0)
            if is_valid_input(s):
                break
            print("Please fix your sequence")

        guess = [COLOR_NUM_MAP[c] for c in [c.upper() for c in s.split(' ')]]
        score = score_guess(guess, t)
        if all([x == 2 for x in score ]):
            print("You've won!!!")
            sys.exit(0)    
        b.append((guess, score))
        os.system('clear') 

         
if __name__ == '__main__':
    main()
    """
    t = generate_target()
    b = []
    for i in range(7):
        g = generate_target()
        s = score_guess(t, g)
        b.append((g,s))
    
    import pprint
    pprint.pprint(b)
    print('')
    draw_board(b)
    input()
    draw_board([(t,[2,2,2,2])])
    """
