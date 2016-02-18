#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        vIdx = {}
        for index, value in enumerate(nums):
            if target - value in vIdx.keys():
                return [vIdx[target-value], index]
            vIdx[value] = index


if __name__ == '__main__':
    nums = [12, 1, 5, 7, 4]
    target = 11
    s = Solution()
    print s.twoSum(nums, target)
