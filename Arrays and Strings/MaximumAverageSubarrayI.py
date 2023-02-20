class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        #fixed window

        #average is the sum / k

        total = 0

        for i in range(k):
            total += nums[i]

        ans = total / k

        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            ans = max(ans, (total/k) )

        return float(ans) / k
