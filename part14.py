#1
class Shape():
    def what_am_i(self):
        print('I am a shape.')
class Square(Shape):
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size
    def what_am_i(self):
        super().what_am_i()
        print('I am a Square.')
square = Square(20)
print(square.square_list)

#2
class Shape():
    def what_am_i(self):
        print('I am a shape.')
class Square(Shape):
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size
    def what_am_i(self):
        super().what_am_i()
        print('I am a Square.')
    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.s1, self.s1, self.s1, self.s1)
square = Square(30)
print(square)

#3
def compare(x, y):
    return x is y
print(compare(10, 100))