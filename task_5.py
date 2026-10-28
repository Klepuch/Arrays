def merge(nums1, m, nums2, n):
    i = m - 1        # останній елемент даних у nums1
    j = n - 1        # останній елемент nums2
    pos = m + n - 1  # куди записувати

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[pos] = nums1[i]
            i -= 1
        else:
            nums1[pos] = nums2[j]
            j -= 1
        pos -= 1


def check(nums1, m, nums2, n, expected):
    original = list(nums1)
    merge(nums1, m, nums2, n)
    print(f"Вхід: nums1 = {original}, m = {m}, nums2 = {nums2}, n = {n}")
    print(f"Вихід:     {nums1}")
    print(f"Очікувано: {expected}")
    print("OK" if nums1 == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    check([1], 1, [], 0, [1])
    check([0], 0, [1], 1, [1])
