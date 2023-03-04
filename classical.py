from random import randint, shuffle


class BlackBox:
    """
    Creates a constant or balanced black box of specified bit length.
    """

    def __init__(self, bit_length, bal_or_const):
        """
        Paramaters
        ----------
        bit_length: int (positive integer)
        bal_or_const: str ('balanced' | 'constant0' | 'constant1')
            'constant0' means the black box to always output 0
            'constant1' means the black box to always output 1
            'balanced' means the black box to output a 1 half of the time and 0 otherwise.
        """

        self.bit_length = bit_length #TODO: positive integer!! PUT LIMIT ON SIZE....64 bit?? 
        self.type = bal_or_const
        self.black_box = self.generate_black_box(bit_length, bal_or_const)

    def generate_black_box(self, bit_length, bal_or_const):
        """
        Generates a (balanced or constant) black box for testing against
        
        Arguments
        ---------
        bit_length: int (positive integer)
        bal_or_const: str ('balanced' | 'constant_0' | 'constant_1')

        Returns
        -------
        black_box: function
            black_box function takes an input of bit_length, and assigns a balanced output or constant output.
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
                black_box = lambda n_bit_string : str(output_list[int(n_bit_string, base=2)])
        elif bal_or_const == 'constant0':
            black_box = lambda n_bit_string : '0'
        elif bal_or_const == 'constant1':
            black_box = lambda n_bit_string : '1'
        return black_box
    
    def generate_rand_n_bits(self, bit_length):
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
 
    def get_output(self, n_bit_string): 
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

    def get_all_inputs(self):
        """
        Gets all possible n-bit inputs for a black box.

        Returns
        -------
        list
            A list of every n-bit input. (Hence the list is of length 2**n).
        """

        n = self.bit_length
        return [str(bin(i))[2:].zfill(n) for i in range(0, 2**n)]

    def get_all_input_output_pairs(self):
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


def determine_classical(black_box_obj):
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