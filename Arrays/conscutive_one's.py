def consecutiv(nums):
    cnt = 0
    maxi_cnt = 0
    for i in range(len(nums)):
        if (nums[i]==1):
            cnt +=1
        else:
            cnt = 0
        maxi_cnt = max(maxi_cnt,cnt)
    return maxi_cnt


arr= [1,1,0,0,1,1,1]
print(consecutiv(arr))