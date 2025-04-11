'''
Heap Solution - O(nlogn) time
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occurences = {}
        for num in nums:
            if num in num_occurences:
                num_occurences[num] += 1
            else:
                num_occurences[num] = 1
        
        max_heap = []
        for num in num_occurences:
            heapq.heappush(max_heap, (-num_occurences[num], num))

        print(max_heap)

        res = []
        for i in range(k):
            val = heapq.heappop(max_heap)
            res.append(val[1])
        
        return res
    
'''
Heap Solution - O(nlogk) time
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occurences = {}
        for num in nums:
            if num in num_occurences:
                num_occurences[num] += 1
            else:
                num_occurences[num] = 1
        
        heap = []
        for key, val in num_occurences.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [element[1] for element in heap]

'''
Linear Time Solution
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        counts_list = [0] * (len(nums)+1)
        for num, freq in counts.items():
            if counts_list[freq] == 0:
                counts_list[freq] = [num]
            else:
                counts_list[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            if counts_list[i] != 0:
                res.extend(counts_list[i])
            if len(res) == k:
                break

        return res