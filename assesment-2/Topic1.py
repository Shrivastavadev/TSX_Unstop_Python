# This is a trial python code
print("Hello World, I am Dev and I am a pro") # to print a line

arr = [2,3,1,8,4,9,5,6,2,22]                  # making an integer array
# using bubble sort to sort the array
for i in range(len(arr)):
    for j in range(len(arr)-1):                 # this has O(n^2) complexity
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],arr[j] # pythony way of swapping elements
print(arr)                                      # there is still room for improvement like stopping if 0 swaps happened in one iteration