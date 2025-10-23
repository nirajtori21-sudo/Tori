def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):   # Inner loop reduces each pass
            if nums[j] > nums[j+1]:  # Swap if out of order
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# Example
print(bubble_sort([5, 3, 8, 6, 2]))  # Output: [2, 3, 5, 6, 8]

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# Example
print(selection_sort([5, 2, 8, 2]))  # Output: [2, 2, 5, 8]

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):          # Start from 1, 0th element is “sorted”
        for j in range(i, 0, -1):  # Move backward
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break               # Stop if already in correct position
    return nums

# Example
print(insertion_sort([5, 3, 8, 6, 2]))  # Output: [2, 3, 5, 6, 8]

