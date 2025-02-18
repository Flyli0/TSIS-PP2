import re
ss = str(input())
sss = re.sub(r'([a-z])([A-Z])', r'\1_\2',ss)
print(sss)