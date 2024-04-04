def countSubarrays(nums, k) -> int:
    mx = max(nums)
    l = countmx = r = res = 0
    allmx = nums.count(mx)
    rdf = allmx // k
    print(mx, allmx, rdf, len(nums))
    while r < len(nums) and l <= r:
        if nums[r] == mx:
            countmx += 1
        if countmx >= k:
            res += 1
        r += 1
        if r == len(nums):
            l += 1
            r = l
            countmx = 0
    return res


nums = [1,3,2,3,3]
k = 2
print(countSubarrays(nums, k))