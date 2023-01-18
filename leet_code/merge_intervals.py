from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        insert_start, insert_end = newInterval

        if not intervals:
            return [newInterval]
        res = []
        new = [newInterval[0],newInterval[1]]

        overlaping = False
        insert = 0

        for i in range(len(intervals)):
            overlap = self.is_overlap(newInterval, intervals[i])
            if intervals[i][1] < insert_start:
                insert += 1
            if not overlap:
                res.append(intervals[i])
            else:
                new = [min(overlap[0], new[0]), max(overlap[1], new[1])]
        res.insert(insert, new)

        return res

    def is_overlap(self, new_interval, other):
        insert_start, insert_end = new_interval
        start, end = other
        if start <= insert_start <= end \
                or start <= insert_end <= end \
                or insert_start <= start <= end <= insert_end:
            return [min(insert_start, start), max(insert_end, end)]
        return None


if __name__ == '__main__':
    print(Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
    print(Solution().insert(intervals=[[1, 2]], newInterval=[2, 8]))
    print(Solution().insert(intervals=[[1, 10]], newInterval=[2, 8]))
    print(Solution().insert(intervals=[[1, 2]], newInterval=[4, 8]))
