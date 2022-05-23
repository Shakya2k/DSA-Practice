class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=set()
        for i in range(n-1):
            for j in range(i+1,n):
                k,l=j+1,n-1
                rem=target-(nums[i]+nums[j])
                while k<l:
                    val=nums[k]+nums[l]
                    if rem==val:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                    elif rem>val:
                        k+=1
                    else:
                        l-=1
        finalres=[]
        for t in res:
            finalres.append(list(t))
        return finalres