from functools import reduce
s = input("enter the word")
rearranged_str = ''.join(sorted(s,key = lambda x: x.upper())).strip()
print(rearranged_str)
