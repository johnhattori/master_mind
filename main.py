#!/usr/bin/env python3

import random
import collections

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

if __name__ == '__main__':
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

