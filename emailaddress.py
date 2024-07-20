import re
import email.utils
n = int(input())
pattern = r'^[a-z][\w\-_.]*[@][a-z]+[.][a-z]{1,3}$'
for i in range(n):
    name, address = email.utils.parseaddr(input())
    if re.match(pattern,address):
        print(email.utils.formataddr((name, address)))
    else:
        continue
