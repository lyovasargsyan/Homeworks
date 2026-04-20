# 1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով: 
#    - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
#    - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
#    - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
#    Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish: 
#    Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
#    - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
#    - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
#    - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:

class Animal:
    def eat(self):
        print("Animal is eating...")
    
    def sleep(self):
        print("Animal is sleeping...")  

class Fish(Animal):
    def swim(self):
        print("Fish is swimming...")

class Bird(Animal):
    def eat(self):
        print("Bird is pecking at its food...")
    
    def fly(self):
        print("Bird is flying...")


animal1 = Animal()
animal1.eat()
animal1.sleep()
print()

bird1 = Bird()
bird1.eat()
bird1.sleep()
bird1.fly()
print()


fish1 = Fish()
fish1.eat()
fish1.swim()
print()



# 2․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
#    Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
#    Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
#    Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի 
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը, 
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։
from abc import ABC, abstractmethod
import math

class Shape:
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...

    @abstractmethod
    def area(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        if radius >= 0:
            self.radius = radius
        else:
            raise AttributeError("Radius must be positive number!!")

    def area(self):
        print(math.pi * self.radius ** 2)

    def perimeter(self):
        print(2 * math.pi * self.radius)


class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__()
        if lenght >= 0:
            self.lenght = lenght
        else:
            raise AttributeError("Lenght must be positive number!!")

        if width >= 0:
            self.width = width
        else:
            raise AttributeError("Width must be positive number!!")
            
    def perimeter(self):
        print(2 * (self.lenght + self.width))
    
    def area(self):
        print(self.lenght * self.width)
    
class Triangle(Shape):
    def __init__(self):
        super().__init__()

    @classmethod
    def area_from_three_sides(cls, a, b, c):
        s = (a + b + c) / 2
        print(math.sqrt(s * (s - a) * (s - b) * (s - c)))
        

    @classmethod
    def area_from_base_height(cls, base, height):
        print(0.5 * base * height)
        

    @classmethod
    def area_from_sides_angle(cls, a, b, angle):
        print(0.5 * a * b * math.sin(math.radians(angle)))
        

    @classmethod
    def perimeter(cls, a, b, c):
        print(a + b + c)

cirlce1 = Circle(5)
cirlce1.area()
cirlce1.perimeter()
print()

rectangle1 = Rectangle(25, 30)
rectangle1.area()
rectangle1.perimeter()
print()

triangle1 = Triangle()
triangle1.area_from_sides_angle(25, 25, 60)
triangle1.area_from_base_height(25, 30)
triangle1.area_from_three_sides(25, 25, 25)
triangle1.perimeter(25, 25, 25)

