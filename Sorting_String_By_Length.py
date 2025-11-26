def sorted_String_length(arr):
    return sorted(arr, key=len)

n = int(input())
string = input().split()

sorted_string = sorted_String_length(string)
print(" ".join(sorted_string))


