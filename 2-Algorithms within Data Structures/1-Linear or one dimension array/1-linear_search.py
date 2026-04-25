# LINEAR SEARCH

def search(arr, target):
    # for each index of the element in the arr length
    for i in range(len(arr)):
        # if the target element exists in the arr[i] of elements
        if arr[i] == target:
            # return the index of the element
            return i
        
arr = [2, 5, 8, 9, 10, 16, 22]
target = 10

print(search(arr, target))