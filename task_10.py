def sort_array_by_parity(nums):
    write = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[write], nums[i] = nums[i], nums[write]
            write += 1

    return nums


def is_valid(nums):
    """Перевірка: після першого непарного не повинно бути парних."""
    seen_odd = False
    for x in nums:
        if x % 2 == 1:
            seen_odd = True
        elif seen_odd:
            return False
    return True


def check(nums, example):
    original = list(nums)
    result = sort_array_by_parity(nums)
    ok = is_valid(result) and sorted(result) == sorted(original)
    print(f"Вхід: nums = {original}")
    print(f"Вихід:     {result}")
    print(f"Приклад правильної відповіді: {example}")
    print("OK" if ok else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([3, 1, 2, 4], [2, 4, 3, 1])
    check([0], [0])
