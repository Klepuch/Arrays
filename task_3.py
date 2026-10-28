def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1

    # Заповнюємо результат з кінця - від найбільшого квадрата
    for pos in range(n - 1, -1, -1):
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1

    return result


def check(nums, expected):
    result = sorted_squares(nums)
    print(f"Вхід: nums = {nums}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100])
    check([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
