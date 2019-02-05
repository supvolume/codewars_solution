""" solution for Ones and Zeros challenge
 convert array that contain 1 and 0 to decimal number """

def binary_array_to_number(arr):
  x=2**(len(arr)-1)
  n=arr[-1]
  for i in arr[:-1]:
      n=n+i*x
      x=x/2
  return n
