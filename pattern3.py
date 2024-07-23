import re

pattern = r"(?<=[^aeiou])([aeiou|AEIOU]{2,})(?=[^aeiou])"
user = input()
match = (re.findall(pattern, user))
for line in match:
  print(line)
if not match:``
print(-1)
