def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Залишки додаємо до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_k_lists(lists):
    if not lists:
        return []

    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2

    left_merged = merge_k_lists(lists[:mid])
    right_merged = merge_k_lists(lists[mid:])

    return merge(left_merged, right_merged)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)

print("Відсортований список:", merged_list)