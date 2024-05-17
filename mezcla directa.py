def merge(arr, left, mid, right):

    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

 
    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr):
    current_size = 1

    while current_size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:

            mid = min((left + current_size - 1), (len(arr) - 1))
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr)-1])
            merge(arr, left, mid, right)
            left = left + current_size * 2


        current_size = 2 * current_size

arr = [38, 27, 43, 3, 9, 82, 10]
print("Array original:", arr)
merge_sort(arr)
print("Array ordenado:", arr)
