class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1.0
        # if x == 0.0:
        #     return 0.0
        # result = 1
        # abs_n = abs(n)
        # for i in range(abs_n):
        #         result *= x
        # if n > 0:
        #     return result
        # else:
        #     return 1/result

        # others:
        if n == 0:
            return 1.0

        result = 1.0
        abs_n = abs(n)

        while abs_n > 0:

            if abs_n % 2 == 1:
                result *= x
            x *= x
            abs_n //= 2


        return result if n > 0 else 1 / result