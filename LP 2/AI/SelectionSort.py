def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i  # assume the current index holds the minimum

        # Find the actual minimum in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap if a smaller element was found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Main Program
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.strip().split()))

    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:  ", sorted_arr)
