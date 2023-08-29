def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    unsorted_list = [12, 11, 13, 5, 6]
    print("Unsorted list:", unsorted_list)
    
    insertion_sort(unsorted_list)
    
    print("Sorted list:", unsorted_list)
