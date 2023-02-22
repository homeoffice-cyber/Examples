# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


class Rectangle(Polygon):
    # Initializing the number of sides of the rectangle by 4
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self, 4)

    def findArea(self):
        a, b, c, d = self.sides

        # Using Heron's formula to calculate the area of the triangle
        area = a * b
        print('The area of the rectangle is %0.2f' % area)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        s = "({0},{1})".format(self.x, self.y)
        print(type(s), s)
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # Creating an instance of the Rectangle class
    # t = Rectangle()

    # Prompting the user to enter the sides of the Rectangle
    # t.inputSides()

    # Displaying the sides of the Rectangle
    # t.dispSides()

    # Calculating and printing the area of the Rectangle
    # t.findArea()

    p1 = Point(0, 2)
    p2 = Point(2, 3)

    print(type(p1))

    print(p1+p2)

#     add comment in py file
# add sone more
#  still learning


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
