def duplicate_zeros(arr):
    n = len(arr)
    zeros = arr.count(0)

    # Йдемо з кінця: i - старий індекс, i + zeros - новий індекс
    for i in range(n - 1, -1, -1):
        if arr[i] == 0:
            # Другий (дубльований) нуль
            if i + zeros < n:
                arr[i + zeros] = 0
            zeros -= 1
            # Перший нуль
            if i + zeros < n:
                arr[i + zeros] = 0
        else:
            if i + zeros < n:
                arr[i + zeros] = arr[i]

    return arr


def check(arr, expected):
    original = list(arr)
    duplicate_zeros(arr)
    print(f"Вхід: arr = {original}")
    print(f"Вихід:     {arr}")
    print(f"Очікувано: {expected}")
    print("OK" if arr == expected else "ПОМИЛКА")
    print()


if __name__ == "__main__":
    check([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4])
    check([1, 2, 3], [1, 2, 3])
    check([0, 0, 0, 0], [0, 0, 0, 0])
