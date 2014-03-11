#!/usr/bin/env python3

import random
import collections

GUESS_SIZE = 4
NUM_COLORS = 6
MAX_GUESSES = 12

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
        if target_map[color] > 0 and score[index] == 0:
            target_map[color] -= 1
            score[index] = 1
    
    score.sort(reverse=True)
    return score

if __name__ == '__main__':
    target = generate_target(GUESS_SIZE, NUM_COLORS)
    guess = generate_target(GUESS_SIZE, NUM_COLORS)
    score = score_guess(guess, target)
    print("%s\n%s\n%s\n" % (target, guess, score))
    
    target = ['y', 'b', 'y', 'b']
    guess = ['y', 'y', 'y', 'b']
    score = score_guess(guess, target)
    print("%s\n%s\n%s\n" % (target, guess, score))


    target = ['r', 'b', 'y', 'b']
    guess = ['y', 'y', 'y', 'b']
    score = score_guess(guess, target)
    print("%s\n%s\n%s\n" % (target, guess, score))

    target = ['r', 'y', 't', 'b']
    guess = ['y', 'y', 't', 't']
    score = score_guess(guess, target)
    print("%s\n%s\n%s\n" % (target, guess, score))
    

