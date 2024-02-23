# Start of "solution.py".

from collections import deque
import copy
import inspect
import time
from typing import List
from typing import Optional
from typing import Set

"""
    Reverse bits of a given 32 bits unsigned integer.

    https://leetcode.com/problems/reverse-bits/
    https://github.com/peniwize/reverse-bits.git

    Note:

        * Note that in some languages, such as Java, there is no unsigned 
        integer type. In this case, both input and output will be given as 
        a signed integer type. They should not affect your implementation, 
        as the integer's internal binary representation is the same, whether 
        it is signed or unsigned.

        * In Java, the compiler represents the signed integers using 2's 
        complement notation. Therefore, in Example 2 above, the input 
        represents the signed integer -3 and the output represents the 
        signed integer -1073741825.

    Constraints:

        * The input must be a binary string of length 32
"""

"""
    Loop through all bits in n and relocate them to alternate side.
    
    Time = O(32) => O(1)

    Space = O(1)
"""
class Solution1_BruteForce:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if n & (1 << i):
                result |= (0x80000000 >> i)
        return result

"""
    Loop through 1/2 of the bits.  For each bit index, calculate a left mask
    and a right mask.  If the bits in n exposed by the masks don't match,
    swap them.
    
    Time = O(16) => O(1)

    Space = O(1)
"""
class Solution2_BruteForce:
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            if 0 != (1 << i) & n:
                if 0 == (0x80000000 >> i) & n:
                    n = (n & ~(1 << i)) | (0x80000000 >> i)
            else:
                if 0 != (0x80000000 >> i) & n:
                    n = (n | (1 << i)) & ~(0x80000000 >> i)
        return n

"""
    Swap adjacect bits, then bit pairs, then nibbles, then bytes, then words.
    This reverses (mirrors) all bits in 'n'.
    
    Time = O(1)

    Space = O(1)
"""
class Solution3_Swap:
    def reverseBits(self, n: int) -> int:
        n = ((n & 0x55555555) << 1) | ((n & 0xaaaaaaaa) >> 1) # Swap adjacent bits.
        n = ((n & 0x33333333) << 2) | ((n & 0xcccccccc) >> 2) # Swap adjacent bit pairs.
        n = ((n & 0x0f0f0f0f) << 4) | ((n & 0xf0f0f0f0) >> 4) # Swap adjacent nibbles.
        n = ((n & 0x00ff00ff) << 8) | ((n & 0xff00ff00) >> 8) # Swap adjacent bytes.
        n = ((n & 0x0000ffff) << 16) | ((n & 0xffff0000) >> 16) # Swap adjacent words.
        return n

def test1(solution): 
    n = 43261596
    expected = 964176192
    startTime = time.time()
    result = solution.reverseBits(n)
    endTime = time.time()
    print("{}:{}({:.6f} sec) result = {}".format(inspect.currentframe().f_code.co_name, type(solution), endTime - startTime, result))
    assert(expected == result)

def test2(solution):
    n = 4294967293
    expected = 3221225471
    startTime = time.time()
    result = solution.reverseBits(n)
    endTime = time.time()
    print("{}:{}({:.6f} sec) result = {}".format(inspect.currentframe().f_code.co_name, type(solution), endTime - startTime, result))
    assert(expected == result)

if "__main__" == __name__:
    test1(Solution1_BruteForce())
    test1(Solution2_BruteForce())
    test1(Solution3_Swap())

    test2(Solution1_BruteForce())
    test2(Solution2_BruteForce())
    test2(Solution3_Swap())

# End of "solution.py".
