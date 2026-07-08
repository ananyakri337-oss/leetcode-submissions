import math
from collections import defaultdict
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        exceptSelf = [] 
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            exceptSelf.append(math.prod(temp))
            
        return exceptSelf