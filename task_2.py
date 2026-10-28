def count_digits(number):
    number = abs(number)
    digits = 1
    while number >= 10:
        number //= 10
        digits += 1
    return digits


def find_numbers(nums):
    count = 0
    for num in nums:
        if count_digits(num) % 2 == 0:
            count += 1
    return count


def check(nums, expected):
    result = find_numbers(nums)
    print(f"Вхід: nums = {nums}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([12, 345, 2, 6, 7896], 2)
    check([555, 901, 482, 1771], 1)
    check([100000], 1)
