'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
'''

'''
What we need to do is to store the number of '1's of every bit. Since each of the 32 bits follow the same rules, we just need to consider 1 bit. We know a number appears 3 times at most, so we need 2 bits to store that. Now we have 4 state, 00, 01, 10 and 11, but we only need 3 of them.

In this solution, 00, 01 and 10 are chosen. Let 'ones' represents the first bit, 'twos' represents the second bit. Then we need to set rules for 'ones' and 'twos' so that they act as we hopes. The complete loop is 00->10->01->00(0->1->2->3/0).

For 'ones', we can get 'ones = ones ^ A[i]; if (twos == 1) then ones = 0', that can be tansformed to 'ones = (ones ^ A[i]) & ~twos'.

Similarly, for 'twos', we can get 'twos = twos ^ A[i]; if (ones* == 1) then twos = 0' and 'twos = (twos ^ A[i]) & ~ones'. Notice that 'ones*' is the value of 'ones' after calculation, that is why twos is
calculated later.

*** TRACK THE BITS NOT THE NUMBER ***
'''

def singleNumber(nums):
  one = two = 0
  for num in nums:
    # add first time: add to one
    one = (one ^ num) & ~two
    # add second time: add to two
    # add third time: remove from two
    two = (two ^ num) & ~one

    # 00: one = (one ^ num) = 1 as two = 0 -> ~two = 1
    #     two = (two ^ num) = 0 as one = 1 -> ~one = 0
    # 10: one = (one ^ num) = 0 as two = 0 -> ~two = 1 (from num back to 0)
    #     two = (two ^ num) = 1 as now one = 0 -> ~one = 1
    # 01: one = (one ^ num) = 0 as two = 1 -> ~two = 0
    #     two = (two ^ num) = 0 as one = 0 -> ~one = 1 (from num back to 0)
  return one

print(singleNumber(nums=[0,1,0,1,0,1,99]))
print(singleNumber(nums=[2,2,3,2]))