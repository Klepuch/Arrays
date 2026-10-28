def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    # Підйом
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # Вершина не може бути першим або останнім елементом
    if i == 0 or i == n - 1:
        return False

    # Спуск
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1


def check(arr, expected):
    result = valid_mountain_array(arr)
    print(f"Вхід: arr = {arr}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([2, 1], False)
    check([3, 5, 5], False)
    check([0, 3, 2, 1], True)
    check([0, 1, 2, 3, 4, 2, 1], True)
    check([0, 2, 3, 3, 5, 2, 1], False)
