#insertion_sort
def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        j = i-1
        key = A[i]
        while j >= 0 and key < A[j]:
            A[j+1] = A[j]
            A[j] = key
            j -= 1
    return A

A = [5,2,4,6,1,3]
insertion_sort(A)
print(A)