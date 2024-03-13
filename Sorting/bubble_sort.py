#bubble_sort
def bubble_sort(A):
    swap = True
    while swap:
        swap = False
        for i in range(1,len(A)):
            if A[i-1] > A[i]:
                temp = A[i-1]
                A[i-1] = A[i]
                A[i] = temp
                swap = True

    

A = [1,9,8,81,76,199,26,21,11,41,38,68]
bubble_sort(A)
print(A)