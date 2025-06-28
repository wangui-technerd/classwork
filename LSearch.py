numbers = [11,22,33,44,55,66,77,88,99]

# key_value = 88
# for i in numbers:
#      if numbers[i] == key_value:
#          print("Found at Pos: {i}")
#          found = True
#          break
# if found is True:
#     print(f"Element {key_value} Found")
# else:
#     print(f"Element {key_value} Not Found")
#
#     # Recursive search practice(code within binary search with a recursive approach)

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

def binary_search(numbers,key):
    start_index= 0
    end_index = len(numbers) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        mid_val = numbers[mid]

        if mid_val == key:
            return mid
        elif key < mid_val:
            end_index = mid - 1
        elif key > mid_val:
            start_index = mid + 1
    return  -1

key = 88

index = binary_search(numbers = numbers, key=key)
# index = binary_search(numbers,key)
print (f"Element Search for Target: {key} found at {index}"if index != -1 else "Target Not Found")

if index != -1:
    print(f"Binary search for Target: {key} found at {index} ")
elif index == -1 :
    print(f"Item not found")

def recursive_binarysearch(num, tar,start,end):
    if start > end:
        return -1

    mid = (start + end ) // 2
    mid_value = num[mid]

    if mid_value == tar:
        return mid
    elif mid_value < tar :
        return  recursive_binarysearch(num,tar,mid+1,end)
    else:
        return recursive_binarysearch(num,tar,start,mid-1)

num = [23,34,45,56,67,78]
tar = 56

index = recursive_binarysearch(num,tar,0,len(num)-1)

if index != -1:
    print(f"Recursive Binary Search: Target {tar} found at {index}")
else:
    print(f"Not found")
