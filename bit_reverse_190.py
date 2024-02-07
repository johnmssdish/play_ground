# # my solution:

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         # num = 43261596
#         # bi_str = format(num, '032b')
#         # print(bi_str)
#         # print(type(bi_str))
#         # r_str = bi_str[::-1]
#         # a = int(r_str, 2)
#         # print(a)
#         # # print(~num)

#         bi_str = format(n, '032b')
#         r_str = bi_str[::-1]
#         return int(r_str,2)



# other solution:
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
