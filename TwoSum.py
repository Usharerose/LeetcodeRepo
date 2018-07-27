#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

"""


class Solution(object):
    @staticmethod
    def twoSum(nums, target):
        """

        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        hash_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_dict:
                return [hash_dict[target - nums[i]], i]
            hash_dict[nums[i]] = i

        return 'Not Found'


if __name__ == '__main__':
    test_list = [2, 7, 11, 15]
    goal = 9
    print(Solution.twoSum(test_list, goal))
