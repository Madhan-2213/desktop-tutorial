import re

nums = int(input())
for _ in range(nums):
  uids = input()
    
  if (len(uids) == 10 and
    uids.isalnum() and
    len(set(uids)) == 10 and
    len(re.findall(r'[A-Z]', uids)) >= 2 and
    len(re.findall(r'\d', uids)) >= 3):
    print("Valid")
  else:
    print("Invalid")
