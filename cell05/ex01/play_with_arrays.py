def main():
    arr = [2, 8, 9, 48, 8, 22, -12, 2]
    print("Original array:", arr)

    for i in range(len(arr)):
        arr[i] += 2
    arr2 = []
    for num in arr:
        if num not in arr2:
            arr2.append(num)
    print("New array:", arr)

main()
