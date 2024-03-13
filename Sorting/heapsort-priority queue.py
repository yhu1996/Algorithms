#heapsort-priority queue 
def parent(i): return (i+1)//2 - 1
def left(i): return 2*i+1
def right(i): return 2*i+2

def Max_heapify(A,i,heap_size):
    max_idx = i
    if left(i) < heap_size and A[max_idx] < A[left(i)]:
        max_idx = left(i)
    if right(i) < heap_size and A[max_idx] < A[right(i)]:
        max_idx = right(i)
    if max_idx != i:
        temp = A[i]
        A[i] = A[max_idx]
        A[max_idx] = temp
        Max_heapify(A,max_idx,heap_size)

def Build_Max_heap(A,heap_size):
    i = parent(heap_size-1)
    while i >= 0:
        Max_heapify(A,i,heap_size)
        i -= 1

def heapsort(A):
    heap_size = len(A)
    while heap_size > 1:
        Build_Max_heap(A,heap_size)
        temp = A[0]
        A[0] = A[heap_size-1]
        A[heap_size-1] = temp
        heap_size -= 1
        
def heap_Max(A): 
    Build_Max_heap(A,len(A))
    return A[0]

def heap_Max_Extract(A):
    Build_Max_heap(A,len(A))
    temp = A[0]
    A[0] = A[-1]
    A.pop()
    Max_heapify(A,0,len(A)-1)
    return temp

def heap_Max_Increase(A,i,key):
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        temp = A[parent(i)]
        A[parent(i)] = A[i]
        A[i] = temp
        i = parent(i)

def heap_Max_Insert(A,key):
    A.append(0)
    heap_Max_Increase(A,len(A)-1,key)


A = [1,9,8,81,76,199,26,21,11,41,38,68]
Build_Max_heap(A,len(A))
print(A)
#maxi = heap_Max(A)
#maxi = heap_Max_Extract(A)
#print(maxi)
#heap_Max_Increase(A,4,200)
heap_Max_Insert(A,200)
print(A)



