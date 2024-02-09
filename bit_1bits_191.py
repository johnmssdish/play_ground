# my solution:
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        n = format(n, '032b')
        for item in n:
            result += int(item)
        return result

# other solution:
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer to binary and remove the '0b' prefix
        binary_representation = bin(n)[2:]
        
        # Count the number of '1' bits in the binary representation
        count_ones = binary_representation.count('1')
        
        return count_ones
