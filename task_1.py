def find_max_consecutive_ones(nums):
    max_count = 0
    current = 0

    for num in nums:
        if num == 1:
            current += 1
            if current > max_count:
                max_count = current
        else:
            current = 0

    return max_count


def check(nums, expected):
    result = find_max_consecutive_ones(nums)
    print(f"Вхід: nums = {nums}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 1, 0, 1, 1, 1], 3)
    check([1, 0, 1, 1, 0, 1], 2)
    check([0], 0)
