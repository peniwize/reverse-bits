/*!
    \file "main.cpp"

    Author: Matt Ervin <matt@impsoftware.org>
    Formatting: 4 spaces/tab (spaces only; no tabs), 120 columns.
    Doc-tool: Doxygen (http://www.doxygen.com/)

    https://leetcode.com/problems/reverse-bits/
    https://github.com/peniwize/reverse-bits.git
*/

//!\sa https://github.com/doctest/doctest/blob/master/doc/markdown/main.md
#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN

#include "utils.hpp"

/*
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
*/

/*
    Time = O(?)

    Space = O(?)
*/
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {

//
//!\todo TODO: >>> Under Construction <<<
//
return 0;

    }
};

// {----------------(120 columns)---------------> Module Code Delimiter <---------------(120 columns)----------------}

namespace doctest {
    const char* testName() noexcept { return doctest::detail::g_cs->currentTest->m_name; }
} // namespace doctest {

TEST_CASE("Case 1")
{
    cerr << doctest::testName() << '\n';
    uint32_t n = 43261596;
    uint32_t const expected = 964176192;
    auto solution = Solution{};
    { // New scope.
        auto const start = std::chrono::steady_clock::now();
        auto const result = solution.reverseBits(n);
        CHECK(expected == result);
        cerr << "Elapsed time: " << elapsed_time_t{start} << '\n';
    }
    cerr << "\n";
}

TEST_CASE("Case 2")
{
    cerr << doctest::testName() << '\n';
    uint32_t n = 4294967293;
    uint32_t const expected = 3221225471;
    auto solution = Solution{};
    { // New scope.
        auto const start = std::chrono::steady_clock::now();
        auto const result = solution.reverseBits(n);
        CHECK(expected == result);
        cerr << "Elapsed time: " << elapsed_time_t{start} << '\n';
    }
    cerr << "\n";
}

/*
    End of "main.cpp"
*/
