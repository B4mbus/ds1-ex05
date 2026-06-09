import matplotlib.pyplot as plt

def merge_sort(list_to_sort_by_merge):
    """
    Sortiert eine Liste in-place mit dem Merge-Sort-Algorithmus.
    """
    if len(list_to_sort_by_merge) > 1:
        # Liste in linke und rechte Hälfte teilen
	mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

	# rekursiver Aufruf auf beiden Hälften
        merge_sort(left)
        merge_sort(right)

        left_idx = 0
        right_idx = 0
        merged_idx = 0

	# left und right sind jetzt sortiert -> immer kleineres Element nehmen
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                list_to_sort_by_merge[merged_idx] = left[left_idx]
                left_idx += 1
            else:
                list_to_sort_by_merge[merged_idx] = right[right_idx]
                right_idx += 1
            merged_idx += 1

	# Falls noch Elemente in left verbleiben -> anhängen
        while left_idx < len(left):
            list_to_sort_by_merge[merged_idx] = left[left_idx]
            left_idx += 1
            merged_idx += 1

	# Falls noch Elemente in right verbleiben -> anhängen
        while right_idx < len(right):
            list_to_sort_by_merge[merged_idx] = right[right_idx]
            right_idx += 1
            merged_idx += 1

if __name__ == "__main__":
    # Visualisierung vor und nach dem Sortieren
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    x = range(len(my_list))
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle("Visualization of list before and after merge sorting")

    # Vor
    ax[0].set_title("Bar chart of unsorted list")
    ax[0].set_xlabel("Index in list")
    ax[0].set_xticks(x)
    ax[0].set_ylabel("Value")
    ax[0].bar(x, my_list)

    # Sort
    merge_sort(my_list)

    # Nach
    ax[1].set_title("Bar chart of sorted list")
    ax[1].set_xlabel("Index in list")
    ax[1].set_xticks(x)
    ax[1].set_ylabel("Value")
    ax[1].bar(x, my_list)

    plt.tight_layout()
    plt.show()
