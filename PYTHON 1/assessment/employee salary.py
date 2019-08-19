company=[("ajay",15000),("s[anu",20000),("arya",25000)]

emp=[name for (name,sal) in company if sal>20000]
print(emp)
print(len(emp))
emp=[name for name in company name.statswith