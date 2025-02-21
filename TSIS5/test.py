import re
s = 'Mission 223'
ss = re.match('^Mission (\d+)',s)
print(ss.group(1))