import re
#x='[abc]' checking for either characters a,b or c
#x='[^abc]'  checking except a,b,c
# x='[a-z]'
x='[A-Z]'
# x='[0-9]'
# x='[a-zA-Z0-9]' print special characters
# x='[^a-zA-Z0-9]' print except special characters
# x='\s' space
# x='\d' any digit
# x='\D' except digit
# x='\w' any word
# x='[\W'] print only special characters
matcher=re.finditer(x,'a7b @k9z')
for match in matcher:
    print("match available at:",match.start())
    print("group:",match.group())
