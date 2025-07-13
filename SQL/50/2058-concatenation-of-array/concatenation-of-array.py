class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
                # Initialize an empty list to store the result
        ans = []
        
        # Loop twice to concatenate nums with itself
        for i in range(2):
            # For each element in nums
            for num in nums:
                # Append the element to ans
                ans.append(num)
        
        # Return the final concatenated list
        return ans