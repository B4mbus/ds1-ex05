def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

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
