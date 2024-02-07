6.  Implement merge sort, upload your code to github and show/test it on the array [5,2,4,7,1,3,2,6].


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    lhs_arr = arr[:mid]
    rhs_arr = arr[mid:]
    
    # Recursively sort each half
    lhs_arr = merge_sort(lhs_arr)
    rhs_arr = merge_sort(rhs_arr)
    
    # Merge the sorted halves
    return merge(lhs_arr, rhs_arr)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Merge both the halves with elements in both
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add remaining elements from the lhs
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Add remaining elements from the rhs
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged

#given array
arr = [5,2,4,7,1,3,2,6]
sorted_arr = merge_sort(arr)
print("This array is sorted by merge sort:", sorted_arr)


OUTPUT:
C:\Users\OMER\Desktop\DAA codes>C:/Python311/python.exe "c:/Users/OMER/Desktop/DAA codes/mergesort.py"
This array is sorted by merge sort: [1, 2, 2, 3, 4, 5, 6, 7]
