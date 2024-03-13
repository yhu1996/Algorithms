#merge
def merge(A1,A2):
    n1 = len(A1)
    n2 = len(A2)
    i = j = 0
    A = []
    while i < n1 and j < n2:
        if A1[i] < A2[j]:
            A.append(A1[i])
            i += 1
        else:
            A.append(A2[j])
            j += 1
    if i < n1:
        for k in range(i,n1):
            A.append(A1[k])
    if j < n2:
        for k in range(j,n2):
            A.append(A2[k])
    return A

A1 = [26,31,41,41,58,68]
A2 = [1,5,8,22,76,199]
A = merge(A1,A2)
print(A)