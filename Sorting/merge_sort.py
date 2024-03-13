#merge_sort
def merge(A,p,q,r):
    A1 = []
    A2 = []
    for i in range(p,q+1):
        A1.append(A[i])
    for i in range(q+1,r+1):
        A2.append(A[i])
    i = j = step = 0
    while i < q-p+1  and j < r-q :
        if A1[i] < A2[j]:
            A[p+step] = A1[i]
            i += 1
        else:
            A[p+step] = A2[j]
            j += 1
        step += 1
    if i < q-p+1:
        for k in range(i,q-p+1):
            A[p+step] = A1[k]
            step += 1
    if j < r-q:
        for k in range(j,r-q):
            A[p+step] = A2[k]
            step += 1

def merge_sort(A,p,r):
    if p < r:
        q = (r+p-1)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    

A = [1,9,8,81,76,199,26,21,11,41,38,68]
merge_sort(A,0,11)
print(A)