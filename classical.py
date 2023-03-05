from random import randint, shuffle
from typing import Callable

from consts import *


class BlackBox:
    """
    Creates a constant or balanced black box of specified bit length.
    """

    def __init__(self, bit_length: int, bal_or_const: BalOrConst):
        """
        Paramaters
        ----------
        bit_length: int (positive integer)
            number of bits for an input to the black box
        bal_or_const: BalOrConst(Enum)
            'CONSTANT_0' means the black box should always output 0
            'CONSTANT_1' means the black box should always output 1
            'BALANCED' means the black box should output a 1 half of the time and 0 otherwise.
       
        Raises
        ------
        ValueError
            if bit_length is not a positive integer less than 24 bits
            or if bal_or_const is not of BalOrConst(Enum) type
        """

        if type(bit_length) is not int or bit_length<1:
            raise ValueError("Bit length must be a positive integer") 
        if bit_length>24:
            raise ValueError("Keep bit length to less than 24 to prevent overloading CPU") 
        if type(bal_or_const) is not BalOrConst:
            raise TypeError('bal_or_const must be of type BalOrConst(Enum)')

        self.bit_length = bit_length 
        self.type = bal_or_const
        self.black_box = self.generate_black_box(bit_length, bal_or_const)

    def generate_black_box(self, bit_length: int, bal_or_const: BalOrConst) -> Callable[[str], str]:
        """
        Generates a (balanced or constant) black box for testing against
        
        Arguments
        ---------
        bit_length: int (positive integer)
        bal_or_const: BalOrConst(Enum)

        Returns
        -------
        black_box: function (n_bit_string -> 1_bit_string)
            black_box function takes an input of bit_length, and assigns a balanced output or constant output.
        """

        black_box = None
        if bal_or_const == BalOrConst.BALANCED:
            if bit_length==1:
                output_list = [0, 1]
                shuffle(output_list)
                black_box = lambda bit_string : str(output_list[int(bit_string)])
            else:
                output_length = 2**bit_length 
                half_output_length = int(output_length/2)
                output_list = [0]*half_output_length + [1]*half_output_length
                shuffle(output_list) # mutates original output_list, to give randomised (balanced) output
                black_box = lambda n_bit_string : str(output_list[int(n_bit_string, base=2)])
        elif bal_or_const == BalOrConst.CONSTANT_0:
            black_box = lambda n_bit_string : '0'
        elif bal_or_const == BalOrConst.CONSTANT_1:
            black_box = lambda n_bit_string : '1'
        return black_box
    
    def generate_rand_n_bits(self, bit_length: int) -> list[int]:
        """
        Generates a random list of n=bit_length bits.

        Arguments
        ---------
        bit_length: int (positive integer)

        Returns
        -------
        list
            A list of n bits.
        """

        return [randint(0,1)]*bit_length
 
    def get_output(self, n_bit_string: str) -> str: 
        """
        Gets the output for any input to the black box

        Arguments
        ---------
        n_bit_string: str
            A length n string of bits. To be considered is input to the black box.
        
        Returns
        -------
        str
            The 1 bit ouput of the black box.
        """
        
        return self.black_box(n_bit_string) 

    def get_all_inputs(self) -> list[str]:
        """
        Gets all possible n-bit inputs for a black box.

        Returns
        -------
        list
            A list of every n-bit input. (Hence the list is of length 2**n).
        """

        n = self.bit_length
        return [str(bin(i))[2:].zfill(n) for i in range(0, 2**n)]

    def get_all_input_output_pairs(self) -> dict:
        """
        Fully determines the black box by computing and returning all of its input-output pairs.

        Useful to print or store the output of this method to understand the black box concretely.

        Returns
        -------
        dict
            The keys are all possible n-bit string inputs, with values the 1-bit outputs of the black box.
        """

        input_list = self.get_all_inputs()
        output_list = [self.black_box(n_bit_string) for n_bit_string in input_list]
        input_output_pairs = zip(input_list, output_list)
        return dict(input_output_pairs)


def determine_classical(black_box_obj: BlackBox) -> str:
    """
    Given a black box, a classical algorithm which tells us if it is constant or balanced.
    
    Runs in O(2**(n-1)) time complexity, for a black box which takes n-bit inputs.
    
    Arguments
    ---------
    black_box_obj: class BlackBox
    
    Returns
    -------
    str
        'balanced' | 'constant'.
    """ 

    bit_length = black_box_obj.bit_length
    black_box = black_box_obj.black_box

    # 1 bit case done seperately
    if(bit_length==1):
        if(black_box('0')==black_box('1')):
            return CONSTANT
        else:
            return BALANCED

    input_list = black_box_obj.get_all_inputs()
    half_input_length = int((2**bit_length)/2)
    constant_bool = True  # Assume constant and try to show its false (i.e. balanced)
    first_output = black_box(input_list[0])
    for i in range(1, half_input_length+1):
        output = black_box(input_list[i])
        constant_bool = constant_bool and (output==first_output)
        if not constant_bool:
            break
    
    return CONSTANT if constant_bool else BALANCED