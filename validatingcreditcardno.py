import re

cc = int(input())
for i in range(cc):
  val_cc = input()
  pattern = (r"^[4-6]\d{3}(-?\d{4}){3}$")
  clean_cc = val_cc.replace("-", "")
  if (re.search(pattern, val_cc)) and len(clean_cc) == 16 and not (re.search(r"(\d)\1{3}", clean_cc)):
    print("Valid")
  else:
    print("Invalid")
