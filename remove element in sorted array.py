# LEETCODE PROBLEM NO 26 = REMOVE DUPLICATED IN SORTED ARRAY

arr=[0,0,1,1,1,2,2,3,3,4]
arr1=set() # or arr1=[]
k=0
for i in range(len(arr)):
    if arr[i] not in arr1:
        arr1.add(arr[i]) # or arr1.append(arr[i])
        arr[k]=arr[i]
        k+=1
print(k)