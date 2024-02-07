
# # my solution:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result_dict = {}
#         for num in nums:
#             if num in list(result_dict.keys()):
#                 result_dict.pop(num)
#             else:
#                 result_dict[num] = 0
#         return list(result_dict.keys())[0]

# ohter solution:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            print(f'result before: {result}')
            print(f'num: {num}')
            result ^= num
            print(f'result after: {result}\n')
            
        return result