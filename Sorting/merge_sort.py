def merge(arr, low, mid, high): 
        # code here
        temp = []
        #[low... mid]
        #[mid+1 .. high]
        
        left = low
        right = mid + 1
        
        
        #Merge elements in sorted order
        while(left<= mid and right <=high):
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left +=1
            else:
                temp.append(arr[right])
                right +=1
            
        
        # Append remaining elements from the left subarray
        while(left<=mid):
            temp.append(arr[left])
            left +=1
            
            
        # Append remaining elements from the right subarray
        while(right<=high):
            temp.append(arr[right])
            right +=1
        
        # Copy the sorted Elements back to the original array
        for i in range(low,high+1):
            arr[i] = temp[i-low]
            
            
            
            
def mergeSort(arr, low, high):
        #code here
    if(low < high):
         
        mid = (high+low)//2
        #Sort the left half
        mergeSort(arr,low,mid)
        #Sort the right half
        mergeSort(arr,mid+1,high)
        #Merge both halves    
        merge(arr,low,mid,high)
        
