#1
class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2
class Square():
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
rectangle = Rectangle(10, 20)
print(rectangle.calculate_perimeter())
square = Square(40)
print(square.calculate_perimeter())

#2
class Square():
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size
square = Square(30)
square.change_size(20)
print(square.s1)

#3
class Shape():
    def what_am_i(self):
        print('I am a shape')
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2
class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
        self.s1 += new_size
rectangle = Rectangle(10, 20)
rectangle.what_am_i()
square = Square(100)
square.what_am_i()

#4
class Rider():
    def __init__(self, name):
        self.name = name
class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider
rider = Rider('John')
horse = Horse('Whillian', rider)
print('The name of Horse is {}'.format(horse.name))
print('The name of Rider is {}'.format(rider.name))