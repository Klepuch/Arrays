def replace_elements(arr):
    max_right = -1

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        if current > max_right:
            max_right = current

    return arr


def check(arr, expected):
    original = list(arr)
    result = replace_elements(arr)
    print(f"Вхід: arr = {original}")
    print(f"Вихід:     {result}")
    print(f"Очікувано: {expected}")
    print("OK" if result == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([17, 18, 5, 4, 6, 1], [18, 6, 6, 6, 1, -1])
    check([400], [-1])
