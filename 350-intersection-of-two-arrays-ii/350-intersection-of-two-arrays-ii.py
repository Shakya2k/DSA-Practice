class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length = min(len(nums1),len(nums2))
        output = []
        hashmap = {}
        if length == len(nums1):
            for i in nums1:
                count = min(nums1.count(i),nums2.count(i))
                if i in nums2 and i not in hashmap.keys():
                    for j in range (count):
                        output.append(i)
                    hashmap[i]=count
        elif length == len(nums2):
            for i in nums2:
                count = min(nums1.count(i),nums2.count(i))
                if i in nums1 and i not in hashmap.keys():
                    for j in range (count):
                        output.append(i)
                    hashmap[i]=count
        return output