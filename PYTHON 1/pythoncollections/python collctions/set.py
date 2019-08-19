
set=set()
print(type(set))
set={10,20,30,40,50,10}
print(set)
set.add(70)
print(set)
set.pop()
print(set)
Day1={"sunday","monday","wednesday","thursday"}
Day2={"monday","thursday,friday"}
print(Day1|Day2)
# print(Day1.union(Day2))
print(Day1&Day2)
# print(Day1.intersection(Day2))
# print(Day1-Day2)
print(Day1.difference(Day2))
# find passed students from a set
Name={"anu","arya","anjana","anju"}
Failed={"anu","anju"}
print(Name-Failed)