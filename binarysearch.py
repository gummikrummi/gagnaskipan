def binary_search(arr,low,high,x): 
    if high >= low: 
        mid = (high + low) // 2 

        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
        else: 
            return binary_search(arr, mid + 1, high, x)  
    else: 
        return None 

my_arr = [2, 5, 7, 20, 100, 105, 207] 
x = 7 
res = binary_search(my_arr, 0, len(my_arr)-1, x)  
print(res)
print(my_arr[res])