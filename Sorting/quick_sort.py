#quick_sort
def partition(A,p,r):
    key = A[r]
    i = p-1 
    # i is the index of the last element in 1st list
    # idx is the index of the last element of 2nd list
    idx = p
    while idx < r:
        if A[idx] <= key:
            # swap A[idx] and A[i+1]
            temp = A[idx]
            A[idx] = A[i+1]
            A[i+1] = temp
            i += 1
        idx += 1
    # swap A[i+1] and A[r], return q = i+1
    A[r] = A[i+1]
    A[i+1] = key
    return i+1
            
            

def quick_sort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)


A = [1,9,8,81,76,199,26,21,11,41,38,68]
quick_sort(A, 0, len(A)-1)
print(A)



