#REMOVE ELEMENTS PROBLEM NO : 27

nums=[3,2,2,3]
val=3
i=0
n=len(nums)
while i< n:
    if nums[i]==val:
        nums[i] = nums[n-1]
        n-=1
    else:
        i+=1
print(n)
