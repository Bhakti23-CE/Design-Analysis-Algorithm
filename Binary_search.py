def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid          
       
        elif arr[mid] > target:
            high = mid - 1
            
        else:
            low = mid + 1
    
    return -1  

arr = [10, 24, 56, 77, 89, 91, 100]
target = 77
result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
