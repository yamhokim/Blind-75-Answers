class Solution:
	def canAttendMeeting(self, intervals: List[List[int]]) -> bool:
		intervals.sort(key = lambda i: i[0])

		for i in range(1, len(intervals)):
			start, end = intervals[i]
			if start < intervals[i - 1][1]:
				return False
		
		return True