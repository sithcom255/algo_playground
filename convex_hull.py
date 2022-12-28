#User function Template for python3

class Solution:
    def FindConvexHull(self, points_list):

        # There must be at least 3 points
        if len(points_list) < 3:
            return  [[-1]]

        # Find the leftmost point
        first = self.find_left_most(points_list)

        result = []

        '''
        Start from leftmost point, keep moving counterclockwise
        until reach the start point again. This loop runs O(h)
        times where h is number of points in result or output.
        '''
        last = first
        next_ = 0
        while(True):

            # Add current point to result
            result.append(last)

            '''
            Search for a point 'q' such that orientation(p, q,
            x) is counterclockwise for all points 'x'. The idea
            is to keep track of last visited most counterclock-
            wise point in q. If any point 'i' is more counterclock-
            wise than q, then update q.
            '''
            next_ = (last + 1) % len(points_list)

            for i in range(len(points_list)):

                # If i is more counterclockwise
                # than current q, then update q
                if self.is_clockwise(points_list[last],
                               points_list[i], points_list[next_]):
                    next_ = i

            '''
            Now q is the most counterclockwise with respect to p
            Set p as q for next iteration, so that q is added to
            result 'hull'
            '''
            last = next_

            # While we don't come to first point
            if(last == first):
                break
        return result

    # Code here

    def is_clockwise(self, a, b, c):
        res = float(c[1] - b[1]) * (b[0] - a[0]) - \
              float(c[0] - b[0]) * (b[1] - a[1])
        return res > 0


    def find_left_most(self, points_list):
        leftmost = 0
        for i, elem in enumerate(points_list):
            if elem[0] < points_list[leftmost][0]:
                leftmost = i
            if elem[0] == points_list[leftmost][0] and elem[1] < points_list[leftmost][1]:
                leftmost = i
        return leftmost

if __name__ == '__main__':
    obj = Solution()
    print(obj.FindConvexHull([[-8, -2], [-5, 10], [8, -6], [6, -10]]))

