class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

    #keep a count of the length of the subarray
    #keep a count of zeros (cannot be greater than k)

    #move left +1 until the constraint is met

    ans = left = count = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            count += 1

        while count > k:
            if nums[left] == 0:
                count -= 1
            left += 1

        ans = max(ans, right-left + 1)

    return ans
