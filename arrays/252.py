# https://leetcode.com/problems/meeting-rooms/
# https://www.lintcode.com/problem/920/description

class Interval:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: list) -> bool:
        """Return True if a person could attend all meetings. Otherwise, return False"""
        intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
