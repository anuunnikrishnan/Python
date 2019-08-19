class Movie:
    def __init__(self,id,moviename,year,rating,duration):
        self.id=id
        self.moviename=moviename
        self.year=year
        self.rating=rating
        self.duration=duration
f=open("movie dataset")
elist=[]
for val in f:
    lst=(val[:-1].split(","))
    elist.append(Movie (lst[0], lst[1], lst[2], lst[3],lst[4]))


