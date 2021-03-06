def bubbleSort(arr): 
  n = len(arr)
  for i in range(n): 
    for j in range(0, n-i-1): 
      if arr[j] > arr[j+1] : 
        arr[j], arr[j+1] = arr[j+1], arr[j]

def selectionSort(arr):
  n = len(arr)
  for i in range(n): 
    min_idx = i 
    for j in range(i+1, len(arr)): 
      if arr[min_idx] > arr[j]: 
        min_idx = j     
    arr[i], arr[min_idx] = arr[min_idx], arr[i] 