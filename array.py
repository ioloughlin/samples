
arr = [0, 0, 9]
roll = False
print(arr)

idx = arr.__len__() - 1

arr[idx] += 1

while idx >= 0:
    if roll is True:
        arr[idx] += 1
        roll = False
    if arr[idx] == 10:
        roll = True
        arr[idx] = 0

    print(arr)
    idx -= 1

if roll is True:
    arr = [1] + arr

print(arr)

