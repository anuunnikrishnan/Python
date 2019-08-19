import re
# x='a'
# x='a+'
# x='a*' check any number of a at individual position
# x='a?' check individual position
# x='a{2}' check for 2 a's'
# x='a{2,5}' check minimum 2 maximum 5
# x='^a' whether the string is starting with a
# x='a$' whether the string is ending with a
matcher=re.finditer(x,"abaabaaabac")
for match in matcher:
    print("position",match.start())
    print("group=",match.group())
