#bubble_sort_v2
def bubble_sort_v2(A):
    n = len(A)
    i = n-1
    while i>0:
        idx_max = i
        for j in range(i):
            if A[idx_max] < A[j]:
                idx_max = j 
        temp = A[i]
        A[i] = A[idx_max]
        A[idx_max] = temp
        i -= 1
    

A = [1,9,8,81,76,199,26,21,11,41,38,68]
bubble_sort(A)
print(A)