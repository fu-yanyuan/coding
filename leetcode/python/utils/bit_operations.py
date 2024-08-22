def flip_one_bit(b):
    # use 1 to XOR
    ''' 
    bit_0 = 0
    bit_1 = 1

    ~ bit_0 = -1   ~ reverse all the bit
    ~ bit_1 = -2

    int(not 0) = 1
    int(not 1) = 0

    1 ^ bit_0 = 1
    1 ^ bit_1 = 0
    '''
    return 1 ^ b

def flip_all_bits(n):
    '''
    5 -> 101
    flip all bits => 010 => 2
    '''
    mask = (1 << n.bit_length()) - 1
    return ~n & mask

def binStr2Int(s):
    return int(s, 2)
