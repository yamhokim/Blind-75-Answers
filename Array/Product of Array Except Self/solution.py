# Solution Using O(N) Space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [1] * len(nums)
        final_products = [1] * len(nums)

        prefix_product = 1
        for num in nums:
            prefix_product *= num
            prefix.append(prefix_product)
        
        postfix_product = 1
        index = len(nums) - 1
        while index >= 0:
            postfix_product *= nums[index]
            postfix[index] = postfix_product
            index -= 1

        for i in range(len(nums)):
            if i == 0:
                pre = 1
                post = postfix[i+1]
            elif i == len(nums) - 1:
                pre = prefix[i - 1]
                post = 1
            else:
                pre = prefix[i - 1]
                post = postfix[i + 1]
            final_products[i] = pre * post
        
        return final_products
    
# Solution Using O(1) Space
class BetterSolution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_products = [1] * len(nums)

        prefix_product = 1
        for i in range(len(nums) - 1):
            prefix_product *= nums[i]
            final_products[i+1] = prefix_product
        
        postfix_product = 1
        index = len(nums) - 1
        while index > 0:
            postfix_product *= nums[index]
            final_products[index - 1] *= postfix_product
            index -= 1

        return final_products