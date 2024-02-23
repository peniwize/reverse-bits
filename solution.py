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

class Solution1_BruteForce:
    def reverseBits(self, n: int) -> int:
        #
        # TODO: >>> Under Construction <<<
        #
        return 0

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

    test2(Solution1_BruteForce())

# End of "solution.py".
