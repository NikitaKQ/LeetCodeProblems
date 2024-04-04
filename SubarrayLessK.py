def numSubarrayProductLessThanK(nums, k):
        l = 0
        n = len(nums)
        product = 1
        ans = 0
        for r in range(n):
            product *= nums[r]
            while l <= r and product >= k:
                # print(l)
                product //= nums[l]
                l += 1
            ans += r - l + 1
        return ans

nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19
print(numSubarrayProductLessThanK(nums, k))
