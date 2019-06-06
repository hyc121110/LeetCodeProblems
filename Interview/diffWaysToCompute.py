'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
'''
import re
import operator

def diffWaysToCompute(self, input):
  # split tokens into numbers and operators
  tokens = re.split('(\D)', input)
  # map integer into numbers idx 0,2,4,...
  nums = map(int, tokens[::2])
  # map operators into +,-,* idx 1,3,5,...
  ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])

  def build(lo, hi):
    if lo == hi:
      return [nums[lo]]
    return [ops[i](a, b) # do operation on a,b (e.g. add(a,b))
            for i in range(lo, hi)
            for a in build(lo, i)
            for b in build(i + 1, hi)]
  return build(0, len(nums) - 1)