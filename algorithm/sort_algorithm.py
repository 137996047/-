# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:22:46 2018

@author: barely
"""
import heapq

class Solution(object):
    
    def partition(self, nums, left, right):
        povit = left
        ix = left + 1
        for l in range(left+1, right+1):
            if nums[l] <= nums[povit]:
                nums[ix], nums[l] = nums[l], nums[ix]
                ix += 1
        nums[povit], nums[ix-1] = nums[ix-1], nums[povit]
        return ix-1
            
    
    def quickSort(self, nums, left, right):
        if left >= right:
            return
        povit = self.partition(nums, left, right)
        self.quickSort(nums, left, povit-1)
        self.quickSort(nums, povit+1, right)

    
    def merge(self, nums, left, mid, right):
        temp = []
        i, j = left, mid+1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        if i <= mid:
            temp += nums[i:mid+1]
        else:
            temp += nums[j:right+1]
        nums[left:right+1] = temp
    
    def mergeSortRecursion(self, nums, left, right):
        if left >= right:
            return 
        mid = (right + left) // 2
        self.mergeSortRecursion(nums, left, mid)
        self.mergeSortRecursion(nums, mid+1, right)
        self.merge(nums, left, mid, right)
    
    def mergeSortIteration(self, nums):
        lenMerge = 1
        lenNums = len(nums)
        while lenMerge < lenNums:
            left = 0
            while left + lenMerge  < lenNums:
                mid = left + lenMerge - 1
                right = mid + lenMerge if mid + lenMerge < lenNums else lenNums - 1
                self.merge(nums, left, mid, right)
                left = right + 1
            lenMerge = lenMerge * 2
            
    def heapSortUsingHeapq(self, nums):3
        heapq.heapify(nums)
        return [heapq.heappop(nums) for i in range(len(nums))]

    def heapify(self, nums, i, end):
        left = 2*i + 1
        right = 2*i + 2
        maxix = i
        if left < end and nums[left] > nums[maxix]:
            maxix = left
        if right < end and nums[right] > nums[maxix]:
            maxix = right
        if i != maxix:
            nums[maxix], nums[i] = nums[i], nums[maxix]
            self.heapify(nums, maxix, end)
    
    def bulidMaxHeap(self, nums):
        i = len(nums) // 2 - 1
        while i >= 0:
            self.heapify(nums, i, len(nums))
            i -= 1
    
    def heapSort(self, nums):
        self.bulidMaxHeap(nums)
        for i in range(len(nums)-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, 0, i)
        
if __name__ == '__main__': 
    test = [100, 5, 8, 6, 45, 21, 34, 89, 22, 12]
    sort = Solution()
    sort.heapSort(test)
    print(test)
    