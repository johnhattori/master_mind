#!usr/bin/env python3

import unittest

from main import * 

class TestScoring(unittest.TestCase):

    def setUp(self):
        pass

    def test_rc_rp(self):
        target = ['y', 'b', 'y', 'b']
        guess = ['y', 'y', 'y', 'b']
        score = score_guess(guess, target)
        assert score == [2,2,2,0]
        
    def test_no_match(self):
        target = ['y','b','r','r']
        guess = [1,1,1,1]
        score = score_guess(guess, target)
        assert score == [0,0,0,0]

    def test_win(self):
        assert [2,2,2] == score_guess(['r','r','r'], ['r','r','r'])

    def test_rc_wp(self):
        assert [1,0,0] == score_guess(['r','g','y'], ['b','r','w'])

    def test_rc_rp_rc_wp(self):
        assert [2,1,0] == score_guess(['r','g','y'], ['r','y','w'])

if __name__ == '__main__':
    unittest.main()

