def check_if_exist(arr):
    seen = set()

    for x in arr:
        if 2 * x in seen:
            return True
        if x % 2 == 0 and x // 2 in seen:
            return True
        seen.add(x)

    return False


def check(arr, expected):
    result = check_if_exist(arr)
    print(f"Вхід: arr = {arr}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([10, 2, 5, 3], True)
    check([3, 1, 7, 11], False)
    check([0, 0], True)
    check([-2, 0, 10, -19, 4, 6, -8], False)
