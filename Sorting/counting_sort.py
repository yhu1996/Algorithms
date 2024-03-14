#counting_sort
def counting_sort(A,k):
    c = [0]*k
    B = [0]*len(A)
    # use c to collect counting of each element i 
    for i in range(len(A)):
        c[A[i]] += 1
    # then make c to record the number of element <= i
    for i in range(1,k):
        c[i] = c[i] + c[i-1]
    # then B[c[i]-1] = i and B is the sorted array 
    for i in range(len(A)):
        B[c[A[i]]-1] = A[i]
        c[A[i]] -= 1
    return B


A = [1,3,4,8,6,9,6,2,1,1,3,8]
B = counting_sort(A,10)
print(B)



