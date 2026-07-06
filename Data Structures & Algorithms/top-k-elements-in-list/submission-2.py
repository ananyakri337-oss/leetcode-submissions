from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictList = defaultdict(int)
        for key in nums:
            dictList[key] += 1
        freqList = sorted(dictList.items(), key=lambda x: x[1], reverse=True)
        outputList = []
        for key, freq in freqList[:k]:
            outputList.append(key)
        return outputList





        