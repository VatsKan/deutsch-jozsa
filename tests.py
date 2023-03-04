# run tests with command: python -m unittest tests
import unittest
from classical import BlackBox, determine_classical

# box = BlackBox(16, 'balanced')
# print(box.get_all_input_output_pairs())

# class TestBlackBox():

class TestClassicalAlgorithm(unittest.TestCase):
    def test_bb_1_bit_bal(self):  
        bb = BlackBox(1, 'balanced') 
        bb_type = determine_classical(bb)
        self.assertTrue(bb.type == bb_type)

    def test_bb_1_bit_const(self):
        bb = BlackBox(1, 'constant0')
        bb_type = determine_classical(bb)
        self.assertTrue('constant' == bb_type)

    def test_bb_2_bit_bal(self):  
        bb = BlackBox(2, 'balanced') 
        bb_type = determine_classical(bb)
        self.assertTrue(bb.type == bb_type)

    def test_bb_2_bit_const(self):
        bb = BlackBox(2, 'constant1')
        bb_type = determine_classical(bb)
        self.assertTrue('constant' == bb_type)

    def test_bb_7_bit_bal(self):  
        bb = BlackBox(7, 'balanced') 
        bb_type = determine_classical(bb)
        self.assertTrue(bb.type == bb_type)

    def test_bb_7_bit_const(self):
        bb = BlackBox(7, 'constant1')
        bb_type = determine_classical(bb)
        self.assertTrue('constant' == bb_type)
        
    def test_bb_16_bit_bal_A(self):  
        bb = BlackBox(16, 'balanced') 
        bb_type = determine_classical(bb)
        self.assertTrue(bb.type == bb_type)

    def test_bb_16_bit_bal_B(self):  
        bb = BlackBox(16, 'balanced') 
        bb_type = determine_classical(bb)
        self.assertTrue(bb.type == bb_type)

    def test_bb_16_bit_const_0(self):
        bb = BlackBox(16, 'constant0')
        bb_type = determine_classical(bb)
        self.assertTrue('constant' == bb_type)

    def test_bb_16_bit_const_1(self):
        bb = BlackBox(16, 'constant1')
        bb_type = determine_classical(bb)
        self.assertTrue('constant' == bb_type)

    def test_bb_21_bit_bal(self):  
        bb = BlackBox(21, 'balanced') 
        bb_type = determine_classical(bb)
        self.assertTrue(bb.type == bb_type)