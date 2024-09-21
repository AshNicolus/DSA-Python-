#oPTIMAL sOLUTION
def removeDuplicate(nums):
    i = 0 
    j = 1
    for j in range(len(nums)):
        if (nums[j] != nums[i]):
            nums[i+1] = nums[j]
            i +=1
    return i +1

arr = [1,1,2,2,2,3,3]
print(removeDuplicate(arr))

