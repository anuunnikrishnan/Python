import re
count=0
matcher=re.finditer('ab','abaababa')
for match in matcher:
    print("match available at:",match.start())
    print("group:",match.group())
    count+=1
print("count :",count)