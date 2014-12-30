__author__ = 'Connor'
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.
def majorityElement(num):
    dic = {}
    for i in range(len(num)):
        if num[i] not in dic:
            dic[num[i]] = 1
        else:
            dic[num[i]] += 1
        if dic[num[i]] >=len(num)/2:
            return num[i]
