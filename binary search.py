#121910313025
#to implement binary search using user defined function
def binarySearch(arr, start, end, x):
# check condition
    if end >= start:
       mid = start + (end- start)//2
   # If element is present at the middle
    if arr[mid] == x:
      return mid
   # If element is smaller than mid
    elif arr[mid] > x:
      return binarySearch(arr, start, mid-1, x)
   # Else the element greator than mid
    else:
      return binarySearch(arr, mid+1, end, x)
arr = sorted(['t','u','t','o','r','i','a','l'])
x ='r'
result = binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
   print("Element is present at index "+str(result))
else:
    print("Element is not present in array")
