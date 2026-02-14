# 4. Отцы, матери и дети

# - Реализуйте два класса: «Родитель» и «Ребёнок». 

# - У родителя есть:
#   -- Имя.
#   -- Возраст.
#   -- Список детей.

# - И он может:
#   -- Сообщить информацию о себе.
#   -- Успокоить ребёнка.
#   -- Покормить ребёнка.

# - У ребёнка есть:
#   -- Имя.
#   -- Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
#   -- Состояние спокойствия.
#   -- Состояние голода.

# - Реализация состояний на ваше усмотрение.
# - Это может быть и простой «флаг», и словарь состояний, и что-нибудь ещё интереснее.


class Parent:
    def __init__(self, name, age, list_of_kids = []):
        self.name = name
        self.age = age
        self.list_of_kids = list_of_kids

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Kids: ')
        for kid in self.list_of_kids:
            print(kid.name)
    

    def calm_down_kid(self, lvl):
        for Kid in self.list_of_kids:
            Kid.calm += lvl
            if Kid.calm > 10:
                Kid.calm = 10
            print(f"{self.name} calmed {Kid.name} down.")

    def feed(self, food_level):
        for Kid in self.list_of_kids:
            Kid.hunger += food_level
            if Kid.hunger > 10:
                Kid.hunger = 10
            print(f"{self.name} feed {Kid.name}.")
    
    @classmethod
    def add_child(cls, parent1, parent2, child_name, child_age):
        if child_age + 16 <= parent1.age and child_age + 16 <= parent2.age:
            child = Child(child_name, child_age)
            parent2.list_of_kids.append(child)
            parent1.list_of_kids.append(child)
        else:
            print("Child's age must be at least 16 year lower than parent's.")



class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.hunger = 5
        self.calm = 5

p1 = Parent("Vazgen", 40)
p2 = Parent("Hripsime" , 34)
Parent.add_child(p1, p2,"Vlad", 7)
p2.add_child(p1, p2, "Anahit" ,11)
p2.feed(3)
p1.calm_down_kid(10)
print()
p1.info()
print()
p2.info()