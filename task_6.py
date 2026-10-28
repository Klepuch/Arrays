def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # перший елемент завжди унікальний
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k


def check(nums, expected_k, expected_prefix):
    original = list(nums)
    k = remove_duplicates(nums)
    shown = nums[:k] + ["_"] * (len(nums) - k)
    print(f"Вхід: nums = {original}")
    print(f"Вихід:     {k}, nums = {shown}")
    print(f"Очікувано: {expected_k}, nums = {expected_prefix} + '_'")
    ok = k == expected_k and nums[:k] == expected_prefix
    print("OK" if ok else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 1, 2], 2, [1, 2])
    check([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4])
