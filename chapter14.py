

class Square:
    square_list = []

    def __init__(self, s, n):
        self.name = n
        self.side = s
        self.square_list.append(self.name)

    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side)


s1 = Square(2, "s1")
s2 = Square(3, "s2")
s3 = Square(4, "s3")
print(Square.square_list)
print(s1)


def same_object(object1, object2):
    return object1 is object2


print(same_object(s1, s2))

