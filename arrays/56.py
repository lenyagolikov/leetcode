# https://leetcode.com/problems/merge-intervals/


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    result = [intervals[0]]

    for current_left, current_right in intervals[1:]:
        last_left, last_right = result[-1]
        if last_right >= current_left:
            result[-1] = [last_left, max(last_right, current_right)]
        else:
            result.append([current_left, current_right])
    return result
