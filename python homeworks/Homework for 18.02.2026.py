# 1․ Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։



class Calculator:
    def __init__(self, number):
        if not isinstance(number, (int, float)):
            raise TypeError("Number must be int or float")
        self.__number = number

    @property
    def num_get(self):
        return self.__number

    def __add__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number / other)

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number // other)

    def __mod__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number % other)

    def __pow__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return Calculator(self.__number ** other)


    def __iadd__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number += other
        return self.__number

    def __isub__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number -= other
        return self.__number

    def __imul__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number *= other
        return self.__number

    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number /= other
        return self.__number

    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number //= other
        return self.__number

    def __imod__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number %= other
        return self.__number

    def __ipow__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        self.__number **= other
        return self.__number

    def __eq__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number == other

    def __ne__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number != other

    def __gt__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number > other

    def __ge__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number >= other

    def __lt__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number < other

    def __le__(self, other):
        if isinstance(other, Calculator):
            other = other.__number
        return self.__number <= other

    def __str__(self):
        return str(self.__number)

    def __repr__(self):
        return f"Calculator(number={self.__number}, type={type(self.__number).__name__})"



c1 = Calculator(10)
c2 = Calculator(3)

print(c1 + c2)  
print(c1 - 2)   
print(c1 * 5)   

c1 += 5
print(c1)        

print(c1 > c2)   
print(repr(c2))  
