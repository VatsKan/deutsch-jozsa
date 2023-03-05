import unittest

from consts import *
from classical import BlackBox, determine_classical


class TestBlackBox(unittest.TestCase):
    def test_black_box_raise_init_errors(self):
        """
        Tests value errors if use wrong initialisation parameters
        """
        self.assertRaises(ValueError, BlackBox, 0, BalOrConst.BALANCED)
        self.assertRaises(ValueError, BlackBox, 32, BalOrConst.BALANCED)
        self.assertRaises(TypeError, BlackBox, 17, 'balanced')

    def test_black_box_generate(self):
        bb = BlackBox(4, BalOrConst.BALANCED)
        self.assertTrue(bb.black_box('0110')=='0' or '1')

    def test_get_all_inputs(self):
        bb = BlackBox(4, BalOrConst.BALANCED)
        input_list = bb.get_all_inputs()
        self.assertTrue(input_list[0]=='0000')
        self.assertTrue(input_list[3]=='0011')
        self.assertTrue(input_list[15]=='1111')
    
    def test_get_output(self):
        bb_A = BlackBox(6, BalOrConst.CONSTANT_0)
        output = bb_A.get_output('100101')
        self.assertTrue(output=='0')

        bb_B = BlackBox(3, BalOrConst.CONSTANT_1)
        output = bb_B.get_output('010')
        self.assertTrue(output=='1')


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