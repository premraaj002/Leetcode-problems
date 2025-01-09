#LEETCODE PROBLEM 88 = MERGE SORTED ARRAY
#APPROACH 1

nums1 = [0]
m = 3
nums2 = [1]
n = 3
#k=[m+n]
a,b=m-1 , n-1
for c in range(m+n-1,-1,-1):
    if a<0:
        nums1[c] = nums2[b]
    elif b<0:
        break
    elif nums1[a]>nums2[b]:
        nums1[c]=nums1[a]
        a-=1
    else:
        nums1[c]=nums2[b]
        b-=1

#APPROACH 2

nums1=[1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
del nums1[m:]
nums1.extend(nums2)
nums1.sort()
print(nums1)