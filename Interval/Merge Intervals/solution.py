class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= res[-1][1]:
                res[-1] = [min(start, res[-1][0]), max(end, res[-1][1])]
            else:
                res.append(intervals[i])

        return res