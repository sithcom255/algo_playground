class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        counter = 0
        negative = False
        if (dividend < 0 and divisor > 0) or \
                (dividend > 0 and divisor < 0):
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        divisor_stack = [(1, divisor)]
        while dividend >= divisor:
            if not divisor_stack:
                break
            increment, divisor_test = divisor_stack[-1]
            if dividend >= divisor_test:
                counter += increment
                dividend = dividend - divisor_test
                divisor_stack.append((increment + increment, divisor_test + divisor_test))
            else:
                divisor_stack.pop()
        if negative:
            counter = - counter
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        counter = min(max(counter, minus_limit), plus_limit)
        return counter


if __name__ == '__main__':
    print(Solution().divide(-2147483648
                            , -1))
