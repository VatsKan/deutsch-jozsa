# TODO: follow PEP guidelines. look at python code structure
# add in error handling. Raising exceptions
# add in docstrings
# add in type checking
# add in tests
# use abstract class as well??
# add in black or flake8
from random import randint, shuffle


class BlackBox:
    """
    Description: Creates a constant or balanced black box of specified bit length.
    """

    def __init__(self, bit_length, bal_or_const):
        # TODO: do some typechecking!! 
        self.bit_length = bit_length #TODO: positive integer!! PUT LIMIT ON SIZE....64 bit?? 
        self.type = bal_or_const
        self.black_box = self.generate_black_box(bit_length, bal_or_const)
        # TODO: generate_black_box_with_QRNG. create an abstract class first

    def generate_black_box(self, bit_length, bal_or_const):
        """ 
        Description: Generates (balanced or constant) black boxes for testing against
        
        Arguments:
        bit_length: integer
        bal_or_const: 'balanced' | 'constant_0' | 'constant_1' 

        Returns:
        function, which takes an input of bit_length, and assigns a balanced output or constant output
        """

        black_box = None
        if bal_or_const == 'balanced':
            if bit_length==1:
                output_list = [0, 1]
                shuffle(output_list)
                black_box = lambda bit_string : str(output_list[int(bit_string)])
            else:
                output_length = 2**bit_length 
                half_output_length = int(output_length/2)
                output_list = [0]*half_output_length + [1]*half_output_length
                shuffle(output_list) # mutates original output_list, to give randomised (balanced) output
                # TODO: Unit Test: output list is of the right length, and balanced!
                black_box = lambda n_bit_string : str(output_list[int(n_bit_string, base=2)])
        elif bal_or_const == 'constant0':
            black_box = lambda n_bit_string : '0'
        elif bal_or_const == 'constant1':
            black_box = lambda n_bit_string : '1'
        # TODO: write unit test for black_boxes in each case.
        return black_box
    
    def generate_rand_n_bits(self, bit_length):
        return [randint(0,1)]*bit_length
 
    def get_output(self, n_bit_string): #TODO: add optional BlackBox parameter
        return self.black_box(n_bit_string) #TODO: allow it to work with arbitrary black box too!

    def get_all_inputs(self):
        n = self.bit_length
        return [str(bin(i))[2:].zfill(n) for i in range(0, 2**n)]

    def get_all_input_output_pairs(self): #TODO: add optional BlackBox parameter
        input_list = self.get_all_inputs()
        output_list = [self.black_box(n_bit_string) for n_bit_string in input_list]
        input_output_pairs = zip(input_list, output_list)
        return dict(input_output_pairs)


def determine_classical(black_box_obj):
    """
    Description: Given a black box, tells us whether it is constant or balanced
    black_box: function(n_bit_string -> 1_bit_string)
    returns: 'balanced' | 'constant'
    """
    
    bit_length = black_box_obj.bit_length
    black_box = black_box_obj.black_box

    # 1 bit case done seperately
    if(bit_length==1):
        if(black_box('0')==black_box('1')):
            return 'constant'
        else:
            return 'balanced'

    input_list = black_box_obj.get_all_inputs()
    half_input_length = int((2**bit_length)/2)
    constant_bool = True  # Assume constant and try to show its false (i.e. balanced)
    first_output = black_box(input_list[0])
    for i in range(1, half_input_length+1):
        output = black_box(input_list[i])
        constant_bool = constant_bool and (output==first_output)
        if not constant_bool:
            break
    
    return 'constant' if constant_bool else 'balanced'