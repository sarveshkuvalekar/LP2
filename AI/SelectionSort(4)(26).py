def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]  
    return arr


arr = list(map(int, input("Enter the array elements (space-separated): ").split()))

print("Original array:", arr)
sorted_arr = selection(arr)
print("Sorted array:", sorted_arr)






# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Find the minimum element in the remaining unsorted array
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         # Swap the found minimum element with the first element
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#         print(f"Step {i+1}: {arr}")  # To show the array at each step

# # Taking input from the user
# n = int(input("Enter the number of elements in the array: "))
# arr = []
# print("Enter the elements of the array:")
# for _ in range(n):
#     arr.append(int(input()))

# print("Initial Array:", arr)
# selection_sort(arr)
# print("Sorted Array:", arr)



