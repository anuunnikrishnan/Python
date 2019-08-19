# class Book1:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self, other):
#         return self.pages+other.pages
#     def __sub__(self, other):
#         return self.pages-other.pages
#     def __mul__(self, other):
#         return self.pages*other.pages
#     def __truediv__(self, other):
#         return self.pages/other.pages
#
# b1=Book1(400)
# b2=Book1(200)
# b3=Book1(300)
# print(b1+b2)
# print(b1-b2)
# print(b1*b2)
# print(b1/b2)

# with 3 objects


class Book1:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        bk=Book1(self.pages + other.pages)
        return bk

    # def __sub__(self, other):
    #     return self.pages - other.pages
    #
    # def __mul__(self, other):
    #     return self.pages * other.pages
    #
    # def __truediv__(self, other):
    #     return self.pages / other.pages
    def __str__(self):
        return str(self.pages)


b1 = Book1(400)
b2 = Book1(200)
b3 = Book1(300)
print(b1+b2+b3)
# print(b1 - b2)
# print(b1 * b2)
# print(b1 / b2)
