#heapsort
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


A = [1,9,8,81,76,199,26,21,11,41,38,68]
heapsort(A)
print(A)



