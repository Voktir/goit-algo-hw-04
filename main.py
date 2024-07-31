from timeit import timeit, default_timer
from random import randint

# Функція сортування злиттям (Merge sort)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Функція сортування вставками (Insertion sort)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Генеруємо масив випадкових цілих чисел
n = 10**4
data = []
for _ in range(n):
    data.append(randint(1, n))

# Вимірюємо час виконання сортування
merge_sort_time = timeit(lambda: merge_sort(data.copy()), number=1)
insertion_sort_time = timeit(lambda: insertion_sort(data.copy()), number=1)
timsort_time_sorted = timeit(lambda: sorted(data.copy()), number=1)

# Виводимо результати
print(f"Merge Sort time: {merge_sort_time:.6f} seconds")
print(f"Insertion Sort time: {insertion_sort_time:.6f} seconds")
print(f"Timsort time_sorted: {timsort_time_sorted:.6f} seconds")