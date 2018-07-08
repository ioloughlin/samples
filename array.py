
arr = [9,9,9,7]
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
    else:
        break
    idx -= 1

if roll is True:
    arr = [1] + arr

print(arr)

