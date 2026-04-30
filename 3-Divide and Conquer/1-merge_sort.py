# <>
# (1) Easy way; with an array of 10 elements

A = [-5, -23, 5, 0, 23, -6, 23, 67]
D = []
while A: 
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimum = x
    D.append(minimum)
    A.remove(minimum)
print(D) 
print(A)

# (2) With an array split into two half: Recursive Merge Sort
def merging(left, right):
    C = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
    return C 

left = [2, 5, 6, 10]
right = [3, 4, 12, 20]
print(merging(left, right))

# Top down method
def sortArray(A):
    if len(A) <= 1:
        return A
    middle = len(A) // 2
    left = sortArray(A[:middle])
    right = sortArray(A[middle:])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

A = [2, 5, 31, 6, 10, 3, 4, 12, 20, 22]
print(sortArray(A))    