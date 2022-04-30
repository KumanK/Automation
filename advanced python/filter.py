def func(arg):
    if type(arg)==str:
        return False
    return True

arr = [10,23,0,'rr',323,'ty']

# arr= list(map(str,arr))
arr= list(map(func,arr))
print(arr)
# arr= list(filter(func,arr))
# print(arr)
