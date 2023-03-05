import unittest

from consts import *
from classical import BlackBox, determine_classical


# class TestBlackBox():


class TestClassicalAlgorithm(unittest.TestCase):
    """
    Tests if the determine_classical function correctly
    finds out if a black box is balanced or constant 
    for a variety of bit-length black boxes.
    """
    
    def test_bb_1_bit_bal(self):  
        bb = BlackBox(1, BalOrConst.BALANCED) 
        bb_type = determine_classical(bb)
        self.assertTrue(BALANCED == bb_type)

    def test_bb_1_bit_const(self):
        bb = BlackBox(1, BalOrConst.CONSTANT_0)
        bb_type = determine_classical(bb)
        self.assertTrue(CONSTANT == bb_type)

    def test_bb_2_bit_bal(self):  
        bb = BlackBox(2, BalOrConst.BALANCED) 
        bb_type = determine_classical(bb)
        self.assertTrue(BALANCED == bb_type)

    def test_bb_2_bit_const(self):
        bb = BlackBox(2, BalOrConst.CONSTANT_1)
        bb_type = determine_classical(bb)
        self.assertTrue(CONSTANT == bb_type)

    def test_bb_7_bit_bal(self):  
        bb = BlackBox(7, BalOrConst.BALANCED) 
        bb_type = determine_classical(bb)
        self.assertTrue(BALANCED == bb_type)

    def test_bb_7_bit_const(self):
        bb = BlackBox(7, BalOrConst.CONSTANT_1)
        bb_type = determine_classical(bb)
        self.assertTrue(CONSTANT == bb_type)
        
    def test_bb_16_bit_bal_A(self):  
        bb = BlackBox(16, BalOrConst.BALANCED) 
        bb_type = determine_classical(bb)
        self.assertTrue(BALANCED == bb_type)

    def test_bb_16_bit_bal_B(self):  
        bb = BlackBox(16, BalOrConst.BALANCED) 
        bb_type = determine_classical(bb)
        self.assertTrue(BALANCED == bb_type)

    def test_bb_16_bit_const_0(self):
        bb = BlackBox(16, BalOrConst.CONSTANT_0)
        bb_type = determine_classical(bb)
        self.assertTrue(CONSTANT == bb_type)

    def test_bb_16_bit_const_1(self):
        bb = BlackBox(16, BalOrConst.CONSTANT_1)
        bb_type = determine_classical(bb)
        self.assertTrue(CONSTANT == bb_type)

    def test_bb_21_bit_bal(self):  
        bb = BlackBox(21, BalOrConst.BALANCED) 
        bb_type = determine_classical(bb)
        self.assertTrue(BALANCED == bb_type)