# 6. Класс «Читать»

# - Создайте класс Читать, который получит в конструкторе ссылку на файл и тип файла.
# - Класс должен уметь читать текстовый файл, json, pickle, изображение (через класс pillow).
# - Для текстового файла напишите методы для
#   -- прочтения текста; 
#   -- печатания первых k строк;
#   -- печатания последних k строк;
#   -- получения текста в виде текста или итератора.
# - Для json и pickle файлов напишите методы для
#   -- получения содержимого.
# - Для изображения напишите методы для
#   -- вывода изображения;
#   -- изменения размера изображения;
#   -- поворачивания изображения на определённый угол, который нужно дать в виде параметра;
#   -- зеркального отражении по горизонтали, по вертикали, по диагонали;
#   -- конвертации изображении в градацию серого;
#   -- сохранения изменённого изображения с новым именем, который нужно дать в виде параметра.

import json
import pickle
from PIL import Image
import os

class Read:
    def __init__(self, file_path, file_type):
        self.file_path = file_path
        self.file_type = file_type
    
    def txt_first(self):
        k = input("Please input how many lines from text start you want get. ")
        l = 1
        with open(self.file_path, "r") as file:
            for i in file:
                print(i)
                if l == k:
                    break
                l += 1

    def txt_last(self):
        k = input("Please input how many lines from text end you want get. ")
        l = 1
        with open(self.file_path, "r") as file:
            for i in file:
                if l == len(file) - k:
                    print(i)
                else:
                    l += 1
    
    def txt_text(self):
        how = input("Please input either <<Text>> or <<Iterator>>!!! ")
        if how.lower() == "text":
            string = ""
            with open(self.file_path, "r") as file:
                for i in file:
                    string += i
            print(string) 
        elif how.lower() == "iterator":
            iterator = []
            with open(self.file_path, "r") as file:
                for i in file:
                    iterator.append(i)
            print(iterator)
        else:
            print("Input is wrong... Please input either <<Text>> or <<Iterator>>!!!")

    def json_read(self):
        with open(self.file_path) as file:
            data = json.load(file)
        print(data)

    def pickle_read(self):
        with open(self.file_path, "wb") as file:
            data = pickle.load(file)
        print(data)

    def image_printer(self):
        img = Image.open(self.file_path)
        img.show()

    def image_size_changer(self):
        height = int(input("Please input image height (in pixels) "))
        width = int(input("Please input image width (in pixels) "))
        img = Image.open(self.file_path)
        resized_img = img.resize((width, height))
        resized_img.show()
    
    def image_rotate(self):
        img = Image.open(self.file_path)
        deg = int(input("Please input how many degrees you want to rotate "))
        rotated_img = img.rotate(deg)
        rotated_img.show()

    def image_mirror(self):
        type_of_change = input("Please input (diagonal, vertical or horzontal) ")
        if type_of_change.lower() == "vertical":
            img = Image.open(self.file_path)
            flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
            flipped.show()
        elif type_of_change == "horizontal":
            img = Image.open(self.file_path)
            mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
            mirrored.show()
        elif type_of_change == "diagonal":
            img = Image.open(self.file_path)
            diagonal = img.transpose(Image.TRANSPOSE)
            diagonal.show()
        else:
            print("Wrong input... Please input (diagonal, vertical or horzontal) ")

    def image_gray(self):
        img = Image.open(self.file_path)
        gray = img.convert("L")
        gray.show()

    def img_change_name(self):
        new_name = input("Please input new name ")
        os.rename(self.file_path, new_name)

    def start(self):
        if self.file_type == "text":
            while True:
                func = input("Please input name of function you want use(txt_first, txt_last, txt_text) or end ")
                if func.lower() == "txt_first":
                    self.txt_first()
                elif func.lower() == "txt_last":
                    self.txt_last()
                elif func.lower() == "txt_text":
                    self.txt_text()
                elif func.lower() == "end":
                    return
                else: 
                    print("Wrong input")
        elif self.file_type.lower() == "json":
            while True:
                func = input("Please input name of function you want use(json_read) ")
                if func.lower() == "json_read":
                    self.json_read()
                elif func.lower() == "end":
                    return
                else: 
                    print("Wrong input")

        elif self.file_type.lower() == "pickle":
            while True:
                func = input("Please input name of function you want use(pickle_read) ")
                if func.lower() == "pickle_read":
                    self.pickle_read()
                elif func.lower() == "end":
                    return
                else: 
                    print("Wrong input")
        
        elif self.file_type.lower() == "image":
            while True:
                func = input("Please input name of function you want use(image_printer, image_mirror, img_change_name, image_gray. image_rotate, image_size_changer) ")
                if func.lower() == "image_printer":
                    self.image_printer()
                elif func.lower() == "image_mirror":
                    self.image_mirror()
                elif func.lower() == "img_change_name":
                    self.img_change_name()
                elif func.lower() == "image_gray":
                    self.image_gray()
                elif func.lower() == "image_rotate":
                    self.image_rotate()
                elif func.lower() == "image_size_changer":
                    self.image_size_changer()
                elif func.lower() == "end":
                    return
                else: 
                    print("Wrong input")

# 8. Магия

# Для данной игры необходимо реализовать механику магии, где при соединении двух
# элементов получается новый. 

# - У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля».
# - Из них как раз и получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

# - Вот таблица преобразований:
#   -- Вода + Воздух = Шторм
#   -- Вода + Огонь = Пар
#   -- Вода + Земля = Грязь
#   -- Воздух + Огонь = Молния
#   -- Воздух + Земля = Пыль
#   -- Огонь + Земля = Лава

# - Напишите программу, которая реализует все эти элементы. 

# - Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается None.

# - Примечание: сложение объектов можно реализовывать через магический метод __add__.

# - Можете изначально создать один класс «Элемент», в котором будете реализовать всю логику магии, 
#   а остальные классы просто будут унаследовать от этого.

# - Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.

class Water:
    def __init__(self, name):
        self.name = name


class Air: 
    def __init__(self, name):
        self.name = name


class Fire:
    def __init__(self, name):
        self.name = name


class Zemlya:
    def __init__(self, name):
        self.name = name


class Shtorm:
    def __init__(self, name):
        self.name = name


class Par:
    def __init__(self, name):
        self.name = name


class Gryaz:   
    def __init__(self, name):
        self.name = name


class Molnia:
    def __init__(self, name):
        self.name = name


class Pil:
    def __init__(self, name):
        self.name = name


class Lava:
    def __init__(self, name):
        self.name = name

    

class Magia:
    def __init__(self, element1, element2):
        self.element1 = element1
        self.element2 = element2

    def mag(self):
        if isinstance(self.element1, Water):
            if isinstance(self.element2, Air):
                self.new_element = Shtorm("shtorm")
            if isinstance(self.element2, Fire):
                self.new_element = Par("par")
            if isinstance(self.element2, Zemlya):
                self.new_element = Gryaz("gryaz")
        elif isinstance(self.element1, Air):
            if isinstance(self.element2, Water):
                self.new_element = Shtorm("shtorm")
            if isinstance(self.element2, Fire):
                self.new_element = Molnia("molnia")
            if isinstance(self.element2, Zemlya):
                self.new_element = Pil("pil")
        elif isinstance(self.element1, Fire):
            if isinstance(self.element2, Zemlya):
                self.new_element = Lava("lava")
            if isinstance(self.element2, Water):
                self.new_element = Par("par")
            if isinstance(self.element2, Air):
                self.new_element = Molnia("molnia")

        return self.new_element
