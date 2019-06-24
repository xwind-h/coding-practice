class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        count = dict()
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            if count[num] > size // 2:
                return num
        return None

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        con = None
        count = 0
        for n in nums:
            if count == 0:
                con = n
            count += 1 if con == n else -1
        return con