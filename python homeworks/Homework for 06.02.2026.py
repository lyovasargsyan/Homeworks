# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
#    - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
#    - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա 
#      (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։
import math

class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or c + b <= a:
            raise ValueError("We can not build triangle with these sides")
        self.a = a
        self.b = b
        self.c = c


    def sides_of_triangles(self):
        print(f'Side A - {self.a}\n' 
              f'Side B - {self.b}\n'
              f'Side C - {self.c}')

    def perimeter(self):
        print(f'Perimeter of our triangle is: {self.a + self.b + self.c}')

    def area(self):
        per = (self.a + self.b + self.c) / 2
        print(f'Area of our triangle is: {round((per * (per - self.a) * (per - self.b) * (per - self.c)) ** (1/2), 2)}')

    def type_of_triangle(self):
        if self.a == self.b and self.a == self.c:
            print("Equilateral triangle")
        elif self.a == self.b or self.a == self.c  or self.c == self.a:
            print("Isosceles triangle")
        else:
            print("Irregular triangle")
    
    def is_right_triangle(self):
        if self.a > self.b and self.a > self.c:
            if (((self.b) ** 2) + ((self.c) ** 2 )) ** (1/2) == self.a:
                print("We have right triangle")
            else:
                print("We do not have right triangle")
        elif self.b > self.a and self.b > self.c:
            if (((self.a) ** 2) + ((self.c) ** 2 )) ** (1/2) == self.b:
                print("We have right triangle")
            else:
                print("We do not have right triangle")
        elif self.c > self.a and self.c > self.b:
            if (((self.a) ** 2) + ((self.b) ** 2 )) ** (1/2) == self.c:
                print("We have right triangle")
            else:
                print("We do not have right triangle")

    def triangle_angles(self):
        print(f'Angle BC - {round(math.acos(math.cos((((self.b ** 2) + (self.c ** 2) - (self.a ** 2)) / (2 * self.c *self.b)))), 2)}\n'
              f'Angle AB - {round(math.acos(math.cos((((self.a ** 2) + (self.c ** 2) - (self.b ** 2)) / (2 * self.a *self.c)))), 2)}\n'
              f'Angle AC - {round(math.acos(math.cos((((self.a ** 2) + (self.b ** 2) - (self.c ** 2)) / (2 * self.a *self.b)))), 2)}')
        
    def inradius(self):
        half_perimeter = (self.a + self.b + self.c) / 2
        area = (half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c)) ** (1/2)
        print(f'Inradius of triangle is: {round(area/half_perimeter, 2)}')
    
    def circumradius(self):
        half_perimeter = (self.a + self.b + self.c) / 2
        area = (half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c)) ** (1/2)
        print(f'Circumradius of triangle is: {round((self.a * self.b * self.c) / (4 * area), 2)}')

        
p1 = Triangle(5, 3, 1)
p1.sides_of_triangles()
p1.perimeter()
p1.area()
p1.type_of_triangle()
p1.is_right_triangle()
p1.triangle_angles()
p1.inradius()
p1.circumradius()