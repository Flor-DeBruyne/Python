from array import array


def BubbleSort(arr):
  n = len(arr)
  for i in range(0, n-2):
    for j in range(n-1, i+1, -1):
      if arr[j-1] > arr[j]:
        tussen = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = tussen